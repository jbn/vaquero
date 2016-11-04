- things almost end up looking like ASM files. And that's okay!
- use orderd dicts. they make debugging real damn easy
- END sentinels (i.e. okay, good, stop processing)
- Add note on clojure influence
- Add note: This is mostly experimental. I use this to continue to play in a 
    open frontiner. But plenty of solutions do this.
- naming convention
- Renaming Effort
- Failure sets
- Non-linearized flow (lasso)
- %run -i convention (actually, some magic)
- Trim execution stack so vaquero is never in path.
- smart sampler (named exceptions)
- refactor unit tests
- enforce 'key': "value" pattern for my strings
- if 'k' exists then -> onto value pattern
- counting collector
- Assertions in the module (pipeline) make sense
    - this is about debugging data, debugging by another name
- use ipython's superreload()
- use unittest assertions in code, and it works?
- look at things like python's block comment -- i.e. reuse of """"""
- for one-off things, the code is not production code. it's held to  a diff 
  standard. but, that doesn't mean there aren't good proactices, they are just
  tailored
- underscores are your friend (conventions. easy to strip. python)
- THIS PATTERN:
    y_col = 'accept'
    X_cols = [k for k in df.columns if k != y_col and not k.startswith('_')]
- envorimental keys? 'staging', 'dev', 'production'
