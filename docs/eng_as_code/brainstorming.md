Motivation - Why we suggest everyone to do EaC

How was daily life of a devloper before?
- Got some customer requirments and located in some tool - need permissions, licenses, approvals and most important you click one requirment and come tomorrow to see the details (very slow)
- Architecture for a software is done in different tool - Images will be used futher for discussions like changes in requirments, design and code
- Requirements done in different tool - and used for design, update architecture if necessary and code
- In ideal case, we assume both architeture and requirments are in sync then we might have wrong requirments or wrong architecture and this lead to complete wrong implementaion and tracebaility
- Architect and requirments discuss and put it in detail desgin and handover to devloper to implement it - different tools
- Developer start implementing the code - no way to test against his requirments
- for testing new person named tester invloves - he needs differnt tool and this generate result - no way to trace back his result against his code and requirements.
- To traceback, we need another person to collect all above information and put into nice excel and say whether its okay or not
- The above case is working in harmony until unless a situtation where no sync happened for a single change in any stage will lead to quality risk

What is Eac ?

Everything in one place and easily testable. Create reports locally.

How it solves the problems we saw in a daily life of developer ?

How we do EaC ?

Keep in one repository
- source code
- detail design
- requirements
- architecture
- test
- test results
- process to trace between "source code - arc - dd - test - test results - req/spec"
- create report
- easy to verify in this approach, if someone modified the source code, we can discuss wherre is the chane in arch , dd, req ?
- Also with help of AI, you can take care all this in one go if you have a req or arch or dd change ?

Details about variant handling - example: take a single component and how the specification to test report we are handling across variants.
- For different variants, we can easily configured for different features using same documentation and trace accordigly. When we generate reports for a single variant we can only see the doc related to the varaint features which are configured.

connection to external requirements management system e.g doors, ..
- we have a concept that anyone can generate CSV or regif format file from your requirements management system.
- This we will convert into json (content, identifier, type, ..)
- Trace it to the next point in v-model

how and why AI is suited for EaC
- Eveything is in one place, so AI can scan through this repository.
- We use skills to develop all software artifacts in the format which is needed to create traceability
