`git commit -a -m 'your message'` will automatically add all files that are being tracked (let's you skip `git add`)

`git log` will show you all versions you've commited
(press q to exit the log, it opens in insert mode for some reason)

`git diff` shows you the difference between the working version and the staged version
If you want to see the difference between the staged version and the repo version, do `git diff --staged`

`git clone github_address` will clone the specified repo to your local directory

`git checkout -b lias_branch` creates a new branch called lias_branch and moves to it
`git checkout master` will move back to the master branch
`git merge lias_branch` will merge lias_branch with the master
`git branch -d lias_branch' will delete the local version of lias_branch
`git push origin :lias_branch` will delete the GitHub version of lias_branch


`git checkout HEAD your_file` will replace the working version of your_file with the last commit

`git reset --hard commit_identifier` will roll back *to* the specified commit and delete all traces in between, the identifier can be found through `git log` I think, you need at least the first 4 digits for it to work

`git resert origin_identifier` will roll back one version *from* the specified commit and create a log of the reversion, you will be required to type of commit message in vi before it will become effective

`git stash` let's you save uncommitted changes so you can return later without committing, I'm not sure exactly how this works but it sounds useful

`HEAD` refers to the most recently committed version
`HEAD~1` refers to the second most recent
etc.

To make git not track something, create a file called `.gitignore' and include the items you want to ignore (can be file extensions, specific files, directories etc.)
Then add and commit this file as normal and these things will not be included in `git status`

