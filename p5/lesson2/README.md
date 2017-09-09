# Lesson 2: Noisy Wave

Congratulations, you survived Lesson 1!  Hopefully you're hungry for more.  In this lesson, we're going to learn a few new programming concepts like **lists** and **for-loops**, we'll learn some new P5 awesomeness, we'll learn about a guy named Ken Perlin, and we'll review functions and step our game up a little bit in that area.  Let's get to it.

## Step 1: Lists and Loops

So, we figured out how to make shapes dance across the browser in the last lesson.  But do you know what's cooler than one shape dancing accross the screen?  A whole bunch of stuff dancing accross the screen!  In JavaScript (and many other languages), there is a construct that helps us to keep track of a bunch of numbers, words, shapes, or anything else.  It's called a list.  You can create a list like this:

```javascript
var fish = ["Platichthys stellatus", "Genyonemus lineatus", "Pimelometopon pulcher"];
// You can also define them on multiple lines:

var birds = [
  "Tachybaptus ruficollis",
  "Ardea cinerea",
  "Mergellus albellus"
];
```

You can then access and modify the items in the lists with **indices**.  An **index** is the location or "place in line" that an item is.  In most programming languages, the first item in the list is at location zero.  The second is at location one.  Etc.  Why zero, you ask?  Imagine a row of mail boxes:

```
 0   1   2   3   4   5   6   7   8
 ---------------------------------
 | a | b | c | d | e | f | g | h |
 ---------------------------------
-8  -7  -6  -5  -4  -3  -2  -1
```

Each mail box contains a letter.  (HA!  Get it??)  One method of selecting items in a list is the `slice` function.  This is going to look weird, but don't freak out.  We'll cover the exact workings of the syntax here later.

```javascript
var letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
letters.splice(3, 2);
// => ['d', 'e']
letters.splice(4, 4);
// => ['e', 'f', 'g', 'h']
```

Does the way we use splice look familiar from Lesson 1?  Sort of?  Function name first, and then parenthesis, with the **arguments** — or inputs — inside.  In this case, the first input is the starting location of the selection.  The second index is how many steps to take.  For the first example we start at index 3 and step over two times:

```
 0   1   2   *-------*   6   7   8   
 ---------------------------------
 | a | b | c | d | e | f | g | h |
 ---------------------------------
```

Splice returns any letters inside the selected area.  The same thing happens in the second example:

```
 0   1   2   3   *---------------*
 ---------------------------------
 | a | b | c | d | e | f | g | h |
 ---------------------------------
```

Another way to select items by **index** works great if you only need one item.

```javascript
var letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
letters[1];
// => 'b'
letters[5];
// => 'f'
```

Notice that, while splice returns a list of values (which you can tell because of the square brackets around them), the second way returns the specific items alone, without enclosing them in a list.

Some other interesting things about lists.  You can have empty ones:

```javascript
var whoops = [];
whoops.length;
// => 0
```

You can have lists with only one item:

```javascript
var lame = [1];
```

Lists can contain different types of things, *including* other lists!

```javascript
var crazy = [1, 'two', 3, 'four', ['five', 'six', 7, 8], '9'];
crazy.length;
// => 6, because the list at index 4 that contains 4 items only counts as one "thing"
crazy[4].length;
// => 4
// You can work with the items as soon as you grab them!
crazy[0] + crazy[2];
// => 4
crazy[2] + crazy[4][3];
// => 11
```

