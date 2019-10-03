# Submission Metadata

Note: The content mentioned here may be subject to change. We will try
not to make backwards incompatible changes to the platform, but we do
reserve the right to make breaking changes to anything described here.

The file `/autograder/submission_metadata.json` contains information
about the current and previous submissions. It contains the following
information:

```
{
  "id": 123456 // Unique identifier for this particular submission
  "created_at": "2018-07-01T14:22:32.365935-07:00", // Submission time
  "assignment": { // Assignment details
    "due_date": "2018-07-31T23:00:00.000000-07:00",
    "group_size": 4, // Maximum group size, or null if not set
    "group_submission": true, // Whether group submission is allowed
    "id": 25828, // Gradescope assignment ID
    "course_id": 1234, // Gradescope course ID
    "late_due_date": null, // Late due date, if set
    "release_date": "2018-07-02T00:00:00.000000-07:00",
    "title": "Programming Assignment 1",
    "total_points": "20.0" // Total point value, including any manual grading portion
    "submission_method": "upload" // Can be "upload", "GitHub", or "Bitbucket"
  },
  "users": [
    {
      "email": "student@example.com",
      "id": 1234,
      "name": "Student User"
    }, ... // Multiple users will be listed in the case of group submissions
  ],
  "previous_submissions": [
    {
      "submission_time": "2017-04-06T14:24:48.087023-07:00",// previous submission time
      "score": 0.0, // Previous submission score
      "results": { ... } // Previous submission results object
    }, ...
  ]
}
```

## Rate limiting schemes

You can use submission_metadata.json to implement arbitrary rate
limiting schemes. For instance, to limit the number of submissions
within a 24 hour period, you can count the number of entries in
`previous_submissions` which are within the last 24 hours, and display
that information in the top level output field.

If a student's submission should be rate limited, you can add a
message to the top level output, and merge that with the results
object from the previous submission. This way, students will keep
their last valid score, but they'll know that they can't submit
anymore.

When implementing such schemes, be sure to compute time periods based
on the current submission's "created_at" (submission time) -
otherwise, re-running the autograder will cause the rate limits to be
computed based on the current system time.
