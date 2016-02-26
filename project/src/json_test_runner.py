"""Running tests"""

import sys
import time
import json

from unittest import result
from unittest.signals import registerResult


class JSONTestResult(result.TestResult):
    """A test result class that can print formatted text results to a stream.

    Used by JSONTestRunner.
    """
    def __init__(self, stream, descriptions, verbosity, results):
        super(JSONTestResult, self).__init__(stream, descriptions, verbosity)
        self.descriptions = descriptions
        self.results = results

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return doc_first_line
        else:
            return str(test)

    def getTags(self, test):
        return getattr(getattr(test, test._testMethodName), '__tags__', None)

    def getWeight(self, test):
        return getattr(getattr(test, test._testMethodName), '__weight__', 0.0)

    def startTest(self, test):
        super(JSONTestResult, self).startTest(test)

    def getOutput(self):
        if self.buffer:
            return self._stdout_buffer.getvalue()

    def buildResult(self, test, passed):
        weight = self.getWeight(test)
        tags = self.getTags(test)
        output = self.getOutput()
        result = {
            "name": self.getDescription(test),
            "score": weight if passed else 0.0,
            "max_score": weight,
        }
        if tags:
            result["tags"] = tags
        if output and len(output) > 0:
            result["output"] = output
        return result

    def addSuccess(self, test):
        super(JSONTestResult, self).addSuccess(test)
        self.results.append(self.buildResult(test, True))

    def addError(self, test, err):
        super(JSONTestResult, self).addError(test, err)
        self.results.append(self.buildResult(test, False))

    def addFailure(self, test, err):
        super(JSONTestResult, self).addFailure(test, err)
        self.results.append(self.buildResult(test, False))


class JSONTestRunner(object):
    """A test runner class that displays results in JSON form.
    """
    resultclass = JSONTestResult

    def __init__(self, stream=sys.stderr, descriptions=True, verbosity=1,
                 failfast=False, buffer=False):
        self.stream = stream
        self.descriptions = descriptions
        self.verbosity = verbosity
        self.failfast = failfast
        self.buffer = buffer
        self.json_data = {}
        self.json_data["tests"] = []

    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity,
                                self.json_data["tests"])

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        startTime = time.time()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        try:
            test(result)
        finally:
            stopTestRun = getattr(result, 'stopTestRun', None)
            if stopTestRun is not None:
                stopTestRun()
        stopTime = time.time()
        timeTaken = stopTime - startTime

        self.json_data["execution_time"] = format(timeTaken, "0.2f")
        json.dump(self.json_data, self.stream, indent=4)
        self.stream.write('\n')
        return result
