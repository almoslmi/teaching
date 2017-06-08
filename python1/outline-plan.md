# Class Outline

## 1: Set the Hook

Initially, I want to minimize the things the students learn.  I want them to blindly do things and marvel at their newfound magical powers.  This section will be entirely devoted to getting them stoked about the possibilities of programming.

 - Use a service like Cloud9 or something where they can get away with not even using the terminal.  Just a play button and a text editor.  Maybe even IDLE would work.

### 1.1: Demonstration (1 day)

I have to come up with some cool programs that I can show them in order to show the power of Python.

 - [X] ~~Web Scraping~~
 - [X] ~~Flask instant website~~
 - Game of Life?
 - [X] ~~Crazy Turtle Spirograph~~
 - Book word data processor
 - Big Prime math problem?
 - Simple game a la pygame?
 - Really fast REPL calculations
 - Plot graph of physics problem?  Maybe whale code
 - [X] ~~Jupyter data analysis~~

### 1.2: Let Them Try (1 day)

The next step is to let them try some things on their own.  I'll have to have something for them to copy, but that they can change and make their own if they figure out how.

Maybe a good idea would be to solve a problem with them, kind of like pair programming but with a bunch of baby navigators!  A simple physics problem codified?  A math problem?  Maybe a combination of the two?

### 1.3: Round-Up (1 day)

Touchy feely.  I want to bring things back to earth and share the schedule/plan/big picture with them.  I want to maybe get a list of their goals for the class, things they are nervous about, things they are excited for, and maybe things they would really like to learn about specifically.  This might be a short day, or maybe I could get them to do some research about something? 
**TODO: Figure something out for the second part of this day**

## 2: First Steps

In this section, I want to start introducing them to things.  This might be a good time for the [the first exploration](first-exploration.md).  My goal for this section is to get them comfortable with writing, looking at, and running code.  They should not be afraid of error messages and should start being able to debug simple things.  It will start with copying code (maybe with some customizations?).  Then we'll move to simple programs, comments, and what good code style basics are like.  This might be a good time to introduce to PEP8!

### 2.1: Our First Program (1-2 days)

We'll work on writing a few simple programs.  We'll introduce variables, math, and numbers/strings.

 - [x] Tip Calculator
 - [x] Greeterbot
 - [x] Repeaterbot
 - [x] Turtle Basics
**TODO: These are some very simple examples.  May need more complicated ones**

### 2.2: Let Them Do It (2-4 days)

In this one, I'll give them a set of requirements and have them create their own program, testing it and running it, etc.  They can submit it to me 3 times or something like that, maybe?  I'll have either multiple times or several choices of projects.  This might be a good time to introduce code review maybe.  I'd have to come up with some guidelines or ways of keeping them from being 💩 faces.

 - [x] ~~Turtle program to write their name~~
 - [x] ~~Turtle program to simulate achilles problem~~
 - User input fractals via turtle?
**TODO: Come up with projects, solution examples**
**TODO: Code review guidelines**

## 3: Basic Framework

This is where I can start to approach a more normalized tutorial approach, teaching the specifics to provide more background knowledge.  I want to definitely do the universe-to-ant style explanation and make sure to always have a mini-map of sorts present so they know where we are, have been, and are going at all times.  This section is where I will start introducing the command line, testing, version control, and some of the other best practices that aren't necessarily code knowledge.
**TODO: Come up with explicit lessons for this section**

### 3.1: Definitions

These next quick sections will be some definitions so the students will have more background.

#### 3.1.1: Overview

This won't take long, but it will be like a micro-syllabus to show what needs covered.

#### 3.1.2: Numbers

This is a good time to go over the different types of numbers, integer vs float, division, etc.

#### 3.1.3: Strings

I think this will be a little longer.  We can talk about adding strings, indexing, how they are immutable.

#### 3.1.4: Function Intro

Introduce functions softly, but completely.  By the end of this section, students will feel start to be able to create their own functions.

#### 3.1.5: Lists

We'll introduce Lists, and discuss indexing once again.  We can start talking about the functions that each type has built onto them.  

#### 3.1.6: Dictionaries

A quick intro to dictionaries and how they are similar and different from lists.  Nothing fancy.

#### 3.1.7: Control Flow

Now we can start to get into some neat stuff.  If statements, For loops, While loops.

### 3.2: Command Line

Now seems like a good time to let things sink in.  I think I'd like to introduce the command line environment now that programming isn't really that scary anymore (hopefully).

#### 3.2.1: File system picture

I want to give them a good idea of what the filesystem looks like so they can hold that image in their head as they stumble around in it.  The sidebar of their editor should help.

#### 3.2.2: Moving Around

`pwd, cd, ls, pushd, popd` to find their way around.  This would be a good time for a folder maze.

#### 3.2.3: Working with Files

`cat, touch, mkdir, rm, mv, rmdir, cp, less, nano`  Maybe a level 2 folder maze.
**TODO: Make level 2 folder maze**

#### 3.2.4: Dip our Toes into Complex Commands

`ssh, grep, find, pipes, and arrows`  The final folder maze.  I want to make sure the students don't feel overwhelmed at this point.
**TODO: Make final folder maze**

#### 3.2.5: Modules

In this section I'll introduce importing, the standard library, and some other notable packages, along with pip.

#### 3.2.6: Running Python Things

Now we can introduce programming things in the terminal.  The REPL, testing, and git!  This section should have two or more projects including the full programming workflow.  Introduce CodeWars? as well.

 - Calculator (my tests)
 - Search - Part 1
 - BIG PROJECT: Book Analyzer
**TODO: Make these project requirement files.**

## 4: Fill in the Gaps

This section will contain a few topics that will expand on things previously covered, or will add additional information.  Pythonic-ness, exceptions, try/except, default args, splats.

### 4.1: Exceptions

This section will work on planned exceptions, try/except clauses and forgiveness rather than permission.

### 4.2: Arguments

This will discuss default arguments, positional, *args and **kwargs.

### 4.3: Pythonic Code

We'll talk about the Tao of Python, working to improve our code quality.  We've already been doing this, but we'll do so even more.  We will introduce list comprehensions too.  I'd like them to do a code review project too.
**TODO: Create several samples of code to be reviewed by students with me and in groups**

## 5: Increase Complexity

This section will be primarily project based.  I want to have them work more and more on harder and harder problems, gaining confidence all the while.  This will be a long section with lots of code reviews and good practices.
**TODO: Come up with good projects and the relevant test suites and related files.**

## 6: Teaser for Next Steps

The things that could possibly be teased.

 - Object Oriented Programming
 - Functional Programming
 - The Web
 - Other Languages
 - Data Science
 - Scientific Python
 - Advanced Python language constructs: Generators, Decorators, etc.