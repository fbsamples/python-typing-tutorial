# Demo Project

In case you are not able to or not interested in setting up type checking on your local machine, you can follow along with most of the Section 2 demo here.

[`greet.py`](https://pyre-check.org/play/?input=def%20greet(subject%3A%20str%2C%20repeat_count%3A%20int)%20-%3E%20None%3A%0A%20%20%20%20greeting%20%3D%20%22Hello%20%22%20%2B%20subject%20%2B%20%22!%22%0A%20%20%20%20for%20_%20in%20range(repeat_count)%3A%0A%20%20%20%20%09print(greeting)%0A%0Adef%20main()%20-%3E%20None%3A%0A%20%20%20%20repeat_count%20%3D%20input(%22Greet%20how%20many%20times%3A%20%22)%0A%20%20%20%20greet(%22World%22%2C%20repeat_count)%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main())