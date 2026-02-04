Contributing
--------------------

[![de](https://img.shields.io/badge/lang-de-blue.svg)](CONTRIBUTING.de.md)

We appreciate submissions of new statistics queries at any time. All submissions will be considered as time allows. We ask your patience; it may require considerable time to decide whether a pull request will be accepted.

Please follow these guidelines when preparing a pull request.

##### Contents
1\. [New contributors](#1-New-contributors)  
2\. [Contributing](#2-Contributing)  
2.1\. [Commits and pull requests](#21-Commits-and-pull-requests)  
2.2\. [Documentation](#22-Documentation)  
2.3\. [Testing](#23-Testing)  
2.4\. [Formatting SQL](#24-Formatting-SQL)  
2.5\. [Naming things](#25-Naming-things)  
3\. [Code review](#3-Code-review)  
4\. [Changelog](#4-Changelog)

1\. New contributors
--------------------

Before beginning work on a contribution, we recommend that you ask the community in advance about the work you propose to do. They may have feedback that would save you time. Please use FOLIO's Slack channel #d-reporting for this purpose. 

You can submit error reports or specific technical suggestions at [Issues](https://github.com/folio-de/d-reporting/issues).


2\. Contributing
-----------------------------


2.1\. Commits and pull requests
-----------------------------

**1. Create fork**

All commits should be made in a “forked” repository, not in this repository.

**2. Branching**

It is strongly recommended to create a new branch in the “forked” repository so that commits are not made directly in the main branch. This means that, if possible, a separate branch should be created for each contribution.

Pull requests are merged. Therefore, the branches for pull requests should be deleted or not reused after merging to avoid confusion. If the main branch is used for a pull request, it is a good idea to re-fork the repository after the merge. 

**3. Pull Request**

It is recommended to keep the scope of the pull request relatively narrow, preferrably addressing only a single issue.

Quoting roughly from the Git Reference Manual, Git commits are documented with a short, one-line title which summarizes the changes, followed by a more thorough, long description. The title should be no more than 75 characters. It is important that at least the title be filled in with a meaningful summary so that the Git history will be readable. Hyperlinks or other references such as "Fixes #" may be included in the long description, but not in the title and not as a substitute for a complete description of the changes.


2.2\. Documentation
-----------------

Each query requires user documentation. The user documentation should contain the following three sections: 

* Purpose 
* Sample output 
* Query instructions, e.g. how to set parameters

Additions or changes to queries should be accompanied by the corresponding additions or changes to user documentation, together in the same pull request.


2.3\. Testing
-----------

All queries or changes to queries should be tested before they are submitted in a pull request. We do not currently have a test data set to allow significant automated testing.


2.4\. Formatting SQL
------------------

Formatting rules are in place to ensure a consistent appearance for SQL queries. These formatting rules can be found under QUERIES.md in the repository.


2.5\. Naming things
-----------------

Names of tables and columns should be in lowercase and use underscores ( _ ) to separate words. Double underscores ( `__` ) should be avoided, as they are used as special indicators in the Metadb, for example.

In the rare case where a column name is both the same as a reserved word and stands alone without a table or alias prefix, it must be enclosed in quotation marks ( " ). Apart from these cases, it is better not to use quotation marks.


3\. Code review
---------------

A pull request is reviewed by at least one person other than the contributor before it can be merged.

If a review suggests expanding the scope of the changes to include additional functionality, those changes do not have to be addressed in the current pull request but may be handled in a separate, new pull request.

The checklist below can be used to guide your review of a pull request (PR). A copy of the checklist may be added to a comment attached to a review. Check off the items that have been confirmed in your review by adding an x between the square brackets [] on each line.

If any items remain unchecked or you have further questions, you can indicate that in the comment as well and select "Request changes" as the review response.

```
- [ ] PR Title and Description are accurate and thorough
- [ ] PR is based on a new branch (not main)
- [ ] PR scope is not overly broad
- [ ] Query runs without errors
- [ ] Query output is correct
- [ ] Query logic is clear and well documented
- [ ] Query is readable and properly indented (formatting rules)
- [ ] Table and column names are in all-lowercase
- [ ] Quotation marks are used only where necessary
- [ ] Query has complete user documentation
    - [ ] Purpose
    - [ ] Sample output
    - [ ] Query instructions
```


4\. Changelog
-----------------------------

The CHANGES.md file is used as a changelog. With each release, the release notes are updated to describe the changes made in the pull requests. TThis should be a self-contained, textual summary of the changes, rather than a hyperlink to an issue.