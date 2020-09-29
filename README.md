# joke-generator

Description:

This web service will:
- retrieve the Full Name that is received by requesting the 'name' from https://api.namefake.com
- pass in the Full Name as part of the payload when requesting the 'joke' from https://api.icndb.com/jokes/random
- return the customized joke, and publish to http://localhost:5000

Instructions:

1. Execute: pip install -r requirements.txt
2. Execute: python3 joke.py
3. Execute: curl localhost:5000

Outstanding Tasks:

1. Setup unittest framework
2. Add unit tests
3. Containerize the solution 