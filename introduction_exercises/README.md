# Introductory Exercises

## Exercises

Each link points to the online Pyre playground.

### Functions

- [Simple function]()
- [Example1](https://pyre-check.org/play?input=%23%20Step%201%3A%20Annotate%20the%20function%20signature%20of%20%60num_vowels%60%3A%20add%20a%20type%0A%23%20annotation%20for%20the%20parameter%20%60input%60%20and%20the%20return%20type.%0A%0A%23%20Step%202%3A%20Identify%20which%20of%20the%20two%20callers%20is%20calling%20this%20function%0A%23%20incorrectly.%20(You%20do%20not%20need%20to%20fix%20the%20bug.)%0A%0Adef%20num_vowels(s)%3A%0A%20%20%20result%20%3D%200%0A%20%20%20for%20letter%20in%20s%3A%0A%20%20%20%20%20%20%20if%20letter%20in%20%22aeiouAEIOU%22%3A%0A%20%20%20%20%20%20%20%20%20%20%20result%20%2B%3D%201%0A%20%20%20return%20result%0A%0A%0Anum_vowels(%22PyCon%20is%20cool%22)%0Anum_vowels(%5B%22PyCon%22%2C%20%22is%22%2C%20%22cool%22%5D)
)

- [Multiple functions](https://pyre-check.org/play?input=%23%20Step%201%3A%20Annotate%20%60get_name%60.%0A%23%20Step%202%3A%20Annotate%20%60greet%60.%0A%23%20Step%203%3A%20Identify%20the%20bug%20in%20%60greet%60.%0A%0Adef%20num_vowels(s%3A%20str)%20-%3E%20int%3A%0A%20%20%20result%20%3D%200%0A%20%20%20for%20letter%20in%20s%3A%0A%20%20%20%20%20%20%20if%20letter%20in%20%22aeiouAEIOU%22%3A%0A%20%20%20%20%20%20%20%20%20%20%20result%20%2B%3D%201%0A%20%20%20return%20result%0A%0Adef%20get_name()%3A%0A%20%20%20return%20%22YOUR%20NAME%20HERE%22%0A%0Adef%20greet(name)%3A%0A%20%20%20print(%22Hello%20%22%20%2B%20name%20%2B%20%22!%20Your%20name%20contains%20%22%20%2B%20num_vowels(name)%20%2B%20%22%20vowels.%22)%0A%0A%23%20Step%204%3A%20Is%20this%20call%20necessary%3F%20Does%20Pyre%20catch%20the%20above%20bug%20even%20without%0A%23%20this%20line%3F%0Agreet(get_name())%0A)

### Classes

- [Simple class](https://pyre-check.org/play?input=class%20Talk%3A%0A%20%20%22%22%22%0A%20%20%3E%3E%3E%20str(Talk(%22Python%20Typing%20Tutorial%22%2C%2013))%0A%20%20%271%20PM%20-%20Python%20Typing%20Tutorial%27%0A%20%20%22%22%22%0A%0A%20%20%23%20Step%201%3A%20Annotate%20the%20constructor.%0A%20%20def%20__init__(self%2C%20title%2C%20hour)%3A%0A%20%20%20%20%20%20self.title%20%3D%20title%0A%20%20%20%20%20%20self.hour%20%3D%20hour%0A%0A%20%20%23%20Step%202%3A%20Annotate%20this%20method.%0A%20%20def%20__str__(self)%3A%0A%20%20%20%20%20%20am_pm_string%20%3D%20%22AM%22%20if%20self.hour%20%3C%2012%20else%20%22PM%22%0A%20%20%20%20%20%20return%20f%22%7Bself.hour%20%25%2012%7D%20%7Bam_pm_string%7D%20-%20%7Bself.title%7D%22%0A%0A%23%20Step%203%3A%20Identity%20the%20bug%20present%20in%20one%20of%20these%20calls.%0ATalk(%22Python%20Typing%20Tutorial%22%2C%20%22right%20now%22)%0ATalk(%22Python%20Typing%20Tutorial%22%2C%2013)%0A)

- [Multiple classes](https://pyre-check.org/play?input=%23%20Step%201%3A%20Annotate%20the%20constructor%20and%20methods%20of%20the%20%60PyCon%60%20class.%0A%23%20Step%202%3A%20Identify%20the%20bug%20present%20in%20one%20or%20more%20of%20the%20three%20calls%20at%20the%20end.%0A%0Aclass%20Talk%3A%0A%20%20%22%22%22%0A%20%20%3E%3E%3E%20str(Talk(%22Python%20Typing%20Tutorial%22%2C%2013))%0A%20%20%271%20PM%20-%20Python%20Typing%20Tutorial%27%0A%20%20%22%22%22%0A%0A%20%20def%20__init__(self%2C%20title%3A%20str%2C%20hour%3A%20int)%20-%3E%20None%3A%0A%20%20%20%20%20%20self.title%20%3D%20title%0A%20%20%20%20%20%20self.hour%20%3D%20hour%0A%0A%20%20def%20__str__(self)%20-%3E%20str%3A%0A%20%20%20%20%20%20am_pm_string%20%3D%20%22AM%22%20if%20self.hour%20%3C%2012%20else%20%22PM%22%0A%20%20%20%20%20%20return%20f%22%7Bself.hour%20%25%2012%7D%20%7Bam_pm_string%7D%20-%20%7Bself.title%7D%22%0A%0Aclass%20PyCon%3A%0A%20%20%20%22%22%22%0A%20%20%20%3E%3E%3E%20pycon%20%3D%20PyCon(%22Salt%20Lake%20City%22%2C%202022)%0A%20%20%20%3E%3E%3E%20pycon.add_talk(Talk(%22Securing%20Code%20with%20the%20Type%20System%22%2C%2011))%0A%20%20%20%3E%3E%3E%20pycon.add_talk(Talk(%22Python%20Typing%20Tutorial%22%2C%2013))%0A%20%20%20%3E%3E%3E%20print(pycon.calendar())%0A%20%20%202022%20PyCon%20at%20Salt%20Lake%20City%0A%20%20%2011%20AM%20-%20Securing%20Code%20with%20the%20Type%20System%0A%20%20%201%20PM%20-%20Python%20Typing%20Tutorial%0A%20%20%20%22%22%22%0A%0A%20%20%20def%20__init__(self%2C%20location%2C%20year)%3A%0A%20%20%20%20%20%20%20self.location%20%3D%20location%0A%20%20%20%20%20%20%20self.year%20%3D%20year%0A%20%20%20%20%20%20%20self.talks%20%3D%20%5B%5D%0A%0A%20%20%20def%20add_talk(self%2C%20talk)%3A%0A%20%20%20%20%20%20%20self.talks.append(talk)%0A%0A%20%20%20def%20calendar(self)%3A%0A%20%20%20%20%20%20%20def%20get_hour(talk)%3A%0A%20%20%20%20%20%20%20%20%20%20%20return%20talk.hour%0A%0A%20%20%20%20%20%20%20sorted_talks%20%3D%20sorted(self.talks%2C%20key%3Dget_hour)%0A%20%20%20%20%20%20%20talks%20%3D%20%22%5Cn%22.join(str(talk)%20for%20talk%20in%20sorted_talks)%0A%20%20%20%20%20%20%20return%20f%22%7Bself.year%7D%20PyCon%20at%20%7Bself.location%7D%5Cn%7Btalks%7D%22%0A%0A%0Apycon%20%3D%20PyCon(%22Salt%20Lake%20City%22%2C%202022)%0Apycon.add_talk(Talk(%22Securing%20Code%20with%20the%20Type%20System%22%2C%2011))%0Apycon.add_talk(%22Python%20Typing%20Tutorial%22)%0Apycon.add_talk(%5BTalk(%22Cool%20Talk%22%2C%2014)%2C%20Talk(%22Cool%20Talk%20II%22%2C%2015)%5D)%0A)

### Data structures

- [Lists](https://pyre-check.org/play?input=%23%20Step%201%3A%20Annotate%20this%20function.%0Adef%20split_into_characters(s)%3A%0A%20%20%22%22%22%0A%20%20%3E%3E%3E%20split_into_characters(%22PyCon%22)%0A%20%20%5B%27P%27%2C%20%27y%27%2C%20%27C%27%2C%20%27o%27%2C%20%27n%27%5D%0A%20%20%22%22%22%0A%20%20return%20%5Bcharacter%20for%20character%20in%20s%5D%0A%0A%23%20Step%202%3A%20Annotate%20this%20function.%0Adef%20strings_to_characters(strings)%3A%0A%20%20%22%22%22%0A%20%20%3E%3E%3E%20strings_to_characters(%5B%22PyCon%22%2C%20%22Typing%22%2C%20%22Tutorial%22%5D)%0A%20%20%5B%5B%27P%27%2C%20%27y%27%2C%20%27C%27%2C%20%27o%27%2C%20%27n%27%5D%2C%20%5B%27T%27%2C%20%27y%27%2C%20%27p%27%2C%20%27i%27%2C%20%27n%27%2C%20%27g%27%5D%2C%20%5B%27T%27%2C%20%27u%27%2C%20%27t%27%2C%20%27o%27%2C%20%27r%27%2C%20%27i%27%2C%20%27a%27%2C%20%27l%27%5D%5D%0A%20%20%22%22%22%0A%20%20return%20%5Bsplit_into_characters(s)%20for%20s%20in%20strings%5D%0A%0A%23%20Step%203%3A%20Identify%20the%20bug%20present%20in%20one%20of%20these%20calls.%0Astrings_to_characters(%5B%22PyCon%22%2C%20%22Typing%22%2C%20%22Tutorial%22%5D)%0Astrings_to_characters(%5B%22PyCon%22%2C%20%22Typing%22%2C%20%22Tutorial%22%2C%202022%2C%20%22is%22%2C%20%22now%22%5D)%0A%0A)

- [Dictionaries and tuples](https://pyre-check.org/play?input=class%20Auditorium%3A%0A%20%20%20%22%22%22%0A%20%20%20%3E%3E%3E%20auditorium%20%3D%20Auditorium(3%2C%208)%0A%20%20%20%3E%3E%3E%20auditorium.add_attendees(%5B(2%2C%203%2C%20%22Shannon%20Zhu%22)%2C%20(3%2C%208%2C%20%22Jia%20Chen%22)%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20(1%2C%206%2C%20%22Alex%20Kassil%22)%2C%20(1%2C%201%2C%20%22Pradeep%20Kumar%22)%5D)%0A%20%20%20%3E%3E%3E%20print(auditorium)%0A%20%20%20PK%20__%20__%20__%20__%20AK%20__%20__%0A%20%20%20__%20__%20SZ%20__%20__%20__%20__%20__%0A%20%20%20__%20__%20__%20__%20__%20__%20__%20JC%0A%20%20%20%22%22%22%0A%0A%20%20%20%23%20Step%201%3A%20Annotate%20this%20constructor.%0A%20%20%20def%20__init__(self%2C%20nrows%2C%20ncolumns)%3A%0A%20%20%20%20%20%20%20%23%20Step%202%3A%20Annotate%20this%20attribute%20explicitly%2C%20since%20it%20is%20not%20being%0A%20%20%20%20%20%20%20%23%20passed%20in%20to%20the%20constructor.%0A%20%20%20%20%20%20%20self.seating%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20row%3A%20%5B%22__%22%20for%20column%20in%20range(ncolumns)%5D%20for%20row%20in%20range(nrows)%0A%20%20%20%20%20%20%20%7D%0A%0A%20%20%20%23%20Step%203%3A%20Annotate%20this%20method.%0A%20%20%20def%20add_attendees(self%2C%20attendees)%3A%0A%20%20%20%20%20%20%20for%20(row%2C%20column%2C%20attendee)%20in%20attendees%3A%0A%20%20%20%20%20%20%20%20%20%20%20first_name%2C%20last_name%20%3D%20attendee.split(%22%20%22)%0A%20%20%20%20%20%20%20%20%20%20%20self.seating%5Brow%20-%201%5D%5Battendee%5D%20%3D%20first_name%5B0%5D%20%2B%20last_name%5B0%5D%0A%0A%20%20%20def%20__str__(self)%20-%3E%20str%3A%0A%20%20%20%20%20%20%20return%20%22%5Cn%22.join(%22%20%22.join(row)%20for%20row%20in%20self.seating.values())%0A%0A%23%20Step%204%3A%20Identify%20a%20bug%20in%20the%20%60add_attendees%60%20method.%20Convince%20yourself%20that%0A%23%20the%20Pyre%20error%20is%20legitimate.%20Did%20you%20catch%20that%20when%20you%20read%20the%20code%3F%0A)

## Running the Exercises Locally

This directory contains exercises related to section 1 of the tutorial.

Every Python file under this directory is a small, self-contained exercise. You can either type check them locally by `cd` into the relevant directory and run `pyre check` to verify your answers, e.g.

```
$ cd functions
$ pyre check
```