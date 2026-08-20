# NOIR Sample Buggy Repo

This tiny repository is intentionally written with security, logic, and maintainability problems.
Use it to demo NOIR's GitHub auto-fix workflow without touching a real project.

## Demo Problems

- unsafe `eval()`
- hardcoded secret key
- deeply nested logic
- unused imports
- empty queue division bug
- weak maintainability

## GitHub Demo Flow

1. Create a new GitHub repo, for example `yourusername/noir-buggy-demo`.
2. Push these files to that repo.
3. From the main NOIR folder, run:

```powershell
python Noir_engine.py yourusername/noir-buggy-demo
```

4. Open GitHub and show the NOIR auto-fix commit.
