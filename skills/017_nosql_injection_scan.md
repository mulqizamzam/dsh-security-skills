## trigger
- keywords: ["mongo", "nosql", "dynamodb", "couch"]
- file_globs: ["**/*mongo*", "**/nosql/**"]
- regex: ["(?i)(\\$where|\\$ne|\\$gt|find\\(|aggregate\\()"]
- ast: ["Call:find", "Call:aggregate"]

## severity
critical

## intent
Prevent operator injection and JavaScript execution in NoSQL queries.

## procedure
1. Reject user-supplied objects in query operators.
2. Enforce type schemas: string stays string.
3. Disable `$where` and `mapReduce` with user input.
4. Reject `$ne: null` auth bypass patterns.
5. Validate ObjectId format before use.
6. For DynamoDB: use expression attribute names/values; never concatenate.
7. For Elasticsearch: reject script fields from user input.

## checks
- [ ] No `$where` from user input
- [ ] Type coercion before query
- [ ] Expression attributes used (Dynamo)
- [ ] No script injection (ES)
- [ ] ObjectId validated

## references
- OWASP NoSQL Injection
- CWE-943

## output
Findings + safe query snippet.
```

---
