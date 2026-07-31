---
description: Perform thorough code review focusing on correctness, readability, maintainability, and best practices
---

## Scope Selection

Before starting the review, determine the scope:

1. **Modified code only** - Review only git changes (recommended for PR reviews)
   - Use `git diff` to see staged changes
   - Use `git diff HEAD~1` to see last commit changes
   - Focus on new/modified functions and their impact

2. **Full codebase review** - Review entire project or specific files
   - Review all files in a directory or module
   - Useful for comprehensive audits or legacy code
   - More time-intensive but thorough

When invoking this workflow, specify which scope you want by mentioning:
- "Review my changes" or "Review git diff" for modified code
- "Review [file/directory]" for full codebase review

## Review Process

When reviewing code, follow this systematic approach:

1. **Correctness & Logic**
   - Verify the code solves the intended problem
   - Check for edge cases and error handling
   - Validate assumptions and invariants
   - Look for potential race conditions or concurrency issues

2. **Readability & Style**
   - Ensure variable/function names are descriptive
   - Check for appropriate comments (not over-commented)
   - Verify consistent code style with project conventions
   - Look for overly complex logic that could be simplified

3. **Maintainability**
   - Check for code duplication (DRY principle)
   - Verify appropriate separation of concerns
   - Look for proper abstraction levels
   - Check if functions/classes have single responsibilities

4. **Performance & Efficiency**
   - Identify unnecessary computations or I/O operations
   - Check for appropriate data structure choices
   - Look for memory leaks or resource cleanup issues
   - Consider algorithmic complexity

5. **Security**
   - Check for input validation and sanitization
   - Look for hardcoded credentials or sensitive data
   - Verify proper error handling doesn't expose information
   - Check for dependency vulnerabilities

6. **Testing**
   - Verify adequate test coverage exists
   - Check if tests cover edge cases
   - Look for brittle or implementation-dependent tests

When providing feedback:
- Be specific and constructive
- Explain why a change is recommended
- Provide examples or alternatives when possible
- Prioritize issues by severity (critical, major, minor)
- Acknowledge good practices you see
