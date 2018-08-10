import os
import json
import xml.etree.ElementTree as et

class NUnitTestCase(object):
    def __init__(self, node, output_map):
        self.node = node
        self.output_map = output_map
        self.load_properties()

    def load_properties(self):
        self.properties = {}
        for property_node in self.node.find('properties').getchildren():
            key = property_node.get('name')
            value = property_node.get('value')
            self.properties[key] = value

    def property(self, key):
        return self.properties.get(key, None)

    def max_score(self):
        if self.property('Weight'):
            return float(self.property('Weight'))
        else:
            return 1.0

    def score(self):
        if self.property('Score'):
            return float(self.property('Score'))
        else:
            if self.node.get('success') == 'True':
                return self.max_score()
            else:
                return 0.0

    def failure(self):
        failure_node = self.node.find('failure')
        if failure_node is not None:
            message_node = failure_node.find('message')
            return message_node.text


    def visibility(self):
        if self.property('Visibility'):
            return self.property('Visibility')

    def name(self):
        if self.property('Name'):
            return self.property('Name')
        else:
            return self.node.get('name')

    def output(self):
        if self.node.get('success') != 'True':
            return self.failure()
        else:
            key = self.node.get('name')
            if key in self.output_map:
                return self.output_map[key]

    def as_dict(self):
        result = {
            "score": self.score(),
            "max_score": self.max_score(),
            "name": self.name()
        }
        if self.visibility():
            result["visibility"] = self.visibility()
        if self.output():
            result["output"] = self.output()
        return result


class NUnitResultsLoader(object):

    def __init__(self):
        self.results = {}
        self.results['stdout_visibility'] = 'hidden'
        self.results['visibility'] = 'visible'
        self.results['tests'] = []
        self.output_map = {}
        self.load_stdout_stderr()

    def load_stdout_stderr(self):
        if os.path.exists('stdout_and_stderr'):
            with open('stdout_and_stderr', 'r') as f:
                data = f.readlines()
                self.process_stdout_stderr(data)

    def process_stdout_stderr(self, data):
        active = False
        current_test = None
        current_output = ""
        for line in data:
            if line.startswith('Tests run:'):
                self.output_map[current_test] = self.output_map[current_test][0:-1]
                break
            if line.startswith('***** '):
                current_test = line[6:-1]
                active = True
                self.output_map[current_test] = ''
            elif active:
                self.output_map[current_test] += line


    def process_results_file(self, filename):
        root = et.parse(filename).getroot()
        self.process_library_suite(root.find('test-suite'))

    def process_library_suite(self, suite_node):
        self.results['execution_time'] = float(suite_node.get('time'))
        for child in suite_node.find('results').getchildren():
            self.process_file_suite(child)

    def process_file_suite(self, suite_node):
        for child in suite_node.find('results').getchildren():
            self.process_test_case(child)

    def process_test_case(self, test_case_node):
        test_case = NUnitTestCase(test_case_node, self.output_map)
        self.results['tests'].append(test_case.as_dict())

    def print_json(self):
        print(json.dumps(self.results))


loader = NUnitResultsLoader()
loader.process_results_file('TestResult.xml')
loader.print_json()

