# Puzzles

In order to level up our programming skills, and have something to do while learning software engineering **workflows**, let's solve some puzzles in Python.

In this repository, you'll find twenty-five folders, each containing one puzzle. Each folder contains a `README.md` with a description of the problem, and a `.py` file with a stub of a solution. Your job is to complete the implementation.

The puzzles, in very approximate order of difficulty, are:

 - leap
 - darts
 - collatz-conjecture
 - scrabble-score
 - anagram
 - acronym
 - isogram
 - pangram
 - word-count
 - rotational-cipher
 - atbash-cipher
 - isbn-verifier
 - pig-latin
 - roman-numerals
 - run-length-encoding
 - say
 - matrix
 - phone-number
 - luhn
 - matching-brackets
 - poker
 - affine-cipher
 - change
 - bowling
 - book-store

Your job, as a team, is to solve as many as possible.

## Setup
 
 1. You've all been assigned to a team that has write access to this repository.
 1. Create a workspace on Gitpod by adding the URL of this repositor
 1. Once the workspace has finished setting up, you might want to enable Autosave from the File menu (I always do this).
 1. The first thing you each should do is create your own version, or **branch** to work on. We'll explain more about this later. For now, type the following:

    ```
    $ git checkout -b your-name-first-branch
    ```

    Substitute your own name, GitHub username, nickname, or initials where you see `your-name` above.

 1. Then, `cd` into whichever puzzle you want to work on, e.g. `leap`:

    ```
    $ cd leap
    ```
 1. Start editing `leap.py`; let's change the `pass` to `return("Party like it's " + str(year))`:

    ```python
    def leap_year(year):
        return("Party like it's " + str(year))
    ```

 1. To try out our code, we _could_ add a print statement to bottom of the file:

    ```python
    def leap_year(year):
        return("Party like it's " + str(year))
    
    print(leap_year(1999))
    ```

    and then run it from the command line:

    ```
    $ python3 leap.py
    Party like it's 1999
    ```

    _but_, instead, I usually find it more helpful to leave the file untouched and run the program interactively. That way I can try it out with a few different inputs:

    ```
    $ python3 -i leap.py
    >>> leap_year(1999)
    "Party like it's 1999"
    >>> leap_year(2000)
    "Party like it's 2000"
    >>>
    ```

    Note that the `-i` flag must come _before_ the filename.

 1. `cd ..` to navigate back up to the parent folder when you're ready to work on a different puzzle, and then `cd` into that one. Rinse and repeat.
 1. Each of you should choose a task to work on. Divide and conquer as you see fit. Before each task, first take a snapshot of the work that you did so far:

    ```
    git commit -A
    git commit -m "A description of what you did"
    ```

    and then switch back to the original version:

    ```
    git checkout master
    ```

    Get the freshest version, in case there have been any updates:

    ```
    git pull
    ```

    And then start a new version for your new task:

    ```
    git checkout -b whatever-my-next-task-is
    ```

    More on this below.

## Python references

 - [The official Python tutorial](https://docs.python.org/3/tutorial/)
 - DataCamp's [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)
 - DataCamp's [Intermediate Python for Data Science](https://www.datacamp.com/courses/intermediate-python-for-data-science)

## Git basics

Git is a very powerful tool with a _lot_ of commands. Here is the small subset of commands that I use a million times a day. We'll add to our toolbelt as time goes on:

 1. To take a snapshot of your work (all of the files and subfolders), use the following two commands from the root folder of the repository:

    ```
    git add -A
    git commit -m "Title of your snapshot"
    ```

 1. Try to make the title somewhat descriptive of what you did since the last snapshot, but it's more important that you just **make lots of commits**. So if you must just say `git commit -m "WIP"` (for "work in progress"), that's fine; we can clean it up later.
 1. Our golden rule: **A**lways **B**e **C**ommitting. As long as you do that, everything will be okay; we can recover from anything with git as long as you commit early and often. You cannot _over_commit but you can most certainly _under_commit.
 1. To see the current status of the repository (are there any changed files since the last commit? etc):

    ```
    git status
    ```
 
 1. To see the line-by-line changes since the last commit:

    ```
    git diff
    ```

 1. To start a new version, or **branch**:

    ```
    git checkout -b fancy-new-version-name
    ```
 1. Again, branch early and often. There's no cost to it and there's lots of benefits to it. In particular, it's good to start a new branch for each _task_ or _feature_. Or just a different approach to the same task, if you want to start over.
 1. To list all branches:

    ```
    git branch
    ```

 1. To switch to another existing branch:

    ```
    git checkout branch-name
    ```

 1. Sometimes, if you have made edits to files that you haven't committed yet, it won't let you switch to another branch. Which is good; you have to make a decision about those changes first — do you want to save them or not? Your options:

    - Make a commit first, and then you can switch to the other branch.
    - If you don't want to pollute your current branch, you can make a new branch, commit the changes, and then switch to the other branch.
    - You can quickly "stash" the changes with `git add -A; git stash`. This puts the changes into a randomly named branch that will eventually be deleted after a few weeks, but until then you can get the changes back if you want them. This is the equivalent of the above, but saves you the trouble of having to think of a name for the new branch.
    
    I usually just think of `git add -A; git stash` as a convenient way to discard all the changes since my most recent commit, so that I can start afresh; but, there _is_ a way to get those changes back if I want them (this only happens about once a year).
 
 1. To see the history of your current branch:

    ```
    git log
    ```

    You will see the author, date, and title of each commit preceded by a long sequence of letters and numbers known as the "SHA-1 hash" of the commit. This is a unique fingerprint of the snapshot.

 1. (Advanced) To jump back to a prior commit:

    ```
    git checkout [SHA of commit you want to go back to]
    ```

    Find the SHA by looking at the output if `git log`. Just the first 7 or so digits of the SHA are enough; you don't need the whole thing.

    If you jump to a commit like this, you'll be in a "detached" state — i.e., not on any branch. This is okay for browsing, but it's best not to make any changes.

    If you want to start a new branch from this point, though, that's perfectly fine — I do that all the time when I decide I want to try a new approach. Just `git checkout -b new-branch-name` as usual.

 1. When you're ready to send the work you've done on a branch back to GitHub.com:

    ```
    git push
    ```

    - The very first time you `push` to a branch, it may ask you to do something like:
        
        ```
        git push --set-upstream origin your-branch-name
        ```
    - The very first time you `push` from Gitpod, it may ask you to give it permission to do so from GitHub. Go ahead and do so. 

 1. To retrieve the freshest version of the branch you're on from GitHub.com, in case there have been any updates:

    ```
    git pull
    ```

 1. When you're ready to start on a new task, the best practice is to first switch back to the `master` branch, get the freshest version, and then to start a new branch from there:

    ```
    git checkout master
    git pull
    git checkout -b my-next-task
    ```

 1. **Never** make commits directly to the `master` branch. Always work on your own, experimental branch. We'll talk about why this is soon.

I know this is a lot, but our main focus today is just getting our feet wet with git. Please wave over an instructor as you experiment with these commands and ask questions; remember:

> Questions are places in your mind where answers fit. If you haven’t asked the question, the answer has nowhere to go. — Clay Christensen
