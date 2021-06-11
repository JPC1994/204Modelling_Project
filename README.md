[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=319138&assignment_repo_type=GroupAssignmentRepo)

# CISC/CMPE 204 Modelling Project

## Summary

Most Queen’s students can agree that course registration is always a bit of a bumpy road – from figuring out what courses can actually be taken based on pre-requisites to fitting all these intended courses into a manageable schedule. These pitfalls of the current system in place have been the inspiration of the project; to create a model for students to plan out their courses based on their respective degree plan. When developing this project, it was crucial to explore various sets of propositions and their constraint relations to encode an algorithm that determines course requirements in the context of graduation.

Throughout the project, various propositions were explored; a set of courses required, a set of courses already taken, a set of courses that can be taken, a list of time slots, credit requirements, and many more. As the scope of the model was streamlined, not all of these propositions made it into the final algorithm. Instead, the focus of the project shifted to looking at a singular degree plan, for a student pursuing a Bachelor in Fundamental Computing (refer to appendix I) and developing a specific list of courses that are related through predicate logic that represent the hierarchical form of their academic journey in the degree path. Specifically, the model now determines what class a student can take with their degree plan and then at what pace they are going to finish their Bachelor. Finally, the model looks at the list of courses taken by the student and determines whether they are eligible to graduate.

## User Interface

The user interface of the model walks through each hypothetical year and semester for the student. It provides a list of possible courses that can be taken, allows the student to “take” the course and then gives the flexibility to move on to planning the consecutive academic semester. Finally at year 4, semester 2, the student can see if they are eligible to graduate. If the student selects a course schedule that satisfies graduation, the program will print out the proposed schedule broken down by year then semester.

## Structure

* `documents`: Contains folders for both draft and final submissions. README.md files are included in both.
* `run.py`: The whole model is implemented within this file.
* `test.py`: This file confirms that our submission has everything required. It shows that we have the right flies and that we have a sufficient theory size.

## Requested Feedback
