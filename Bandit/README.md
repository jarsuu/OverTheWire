# Bandit
## Level 0
To connect to the game, run the command:\
`ssh -p 2220 bandit0@bandit.labs.overthewire.org`\
with the password as `bandit0`

## Level 1
Read the file contents of **readme**:\
`cat readme`

The password:\
`ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

Login to bandit1:\
`ssh -p 2220 bandit1@bandit.labs.overthewire.org`\
with the password from above

## Level 2
To read a dashed filename:\
`cat < -`\
Source: [Stack Overflow](https://stackoverflow.com/questions/42187323/how-to-open-a-dashed-filename-using-terminal)

The password:\
`263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

Login to bandit2 like above

## Level 3
Read **spaces in this filename**:\
`cat "spaces in this filename"`

Password:
`MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

## Level 4
Find the hidden directory **inhere** and hidden password file:\
1. `ls -a` -> list all hidden files
2. `cd inhere`
3. `ls -a`
4. `cat ...Hiding-From-You`

Password:\
`2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

## Level 5
Find the file types in **inhere**:\
`file inhere/*`

Output:
```
inhere/-file00: data
inhere/-file01: data
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data
inhere/-file05: data
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
```
where `inhere/-file07` is the human-readable format file.

Password:\
`4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

## Level 6
Find file:
`find inhere/ -type f -size 1033c ! -executable`\
where:\
`-type f` = file type\
`-size 1033c` = 1033 bytes\
`! -executable` = not executable

Output:\
`inhere/maybehere07/.file2: ASCII text, with very long lines (1000)`

Password:\
`HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

## Level 7
Find a file somehwere in the server meeting conditions:
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

Command:\
`find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null`\
where:\
`/` = root directory
`2>/dev/null` = filters out permission denied files

Output:\
`/var/lib/dpkg/info/bandit7.password`

Password:\
`morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

## Level 8
...