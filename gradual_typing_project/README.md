# Gradual Typing Project

In case you are not able to or not interested in setting up type checking on your local machine, you can follow along with the first slide of the Section 3 demo here.


[`main.py`](https://pyre-check.org/play?input=import%20json%0Afrom%20typing%20import%20*%0A%0A%23%20from%20park.py%0Aclass%20Park%3A%0A%20%20%20%20def%20__init__(self)%3A%0A%20%20%20%20%20%20%20%20self.inside_park%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22cats%22%3A%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22dogs%22%3A%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20self.outside_park%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22cats%22%3A%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22dogs%22%3A%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20def%20populate(self%2C%20input)%3A%20...%0A%20%20%20%20def%20simulate_hour(self)%3A%20...%0A%0A%23%20from%20main.py%0Adef%20get_cat_dog_ratio(park)%3A%0A%20%20%20%20cats%20%3D%20len(park.inside_park%5B%22cats%22%5D)%0A%20%20%20%20dogs%20%3D%20len(park.inside_park%5B%22dogs%22%5D)%0A%20%20%20%20print(f%22There%20are%20%7Bcats%7D%20cats%20and%20%7Bdogs%7D%20dogs%20in%20the%20park.%22)%0A%20%20%20%20return%20cats%20%2F%20dogs%0A%0A%0Adef%20run(park)%3A%0A%20%20%20%20for%20hour%20in%20range(1%2C%209)%3A%0A%20%20%20%20%20%20%20%20print(f%22Hour%3A%20%7Bhour%7D%22)%0A%20%20%20%20%20%20%20%20cat_dog_ratio%20%3D%20get_cat_dog_ratio(park)%0A%20%20%20%20%20%20%20%20dog_cat_ratio%20%3D%201%20%2F%20cat_dog_ratio%0A%20%20%20%20%20%20%20%20print(%22Ratio%20of%20cats%20to%20dogs%20is%22%20%2B%20cat_dog_ratio)%0A%20%20%20%20%20%20%20%20print(%22Ratio%20of%20dogs%20to%20cats%20is%20%22%20%2B%20dog_cat_ratio)%0A%20%20%20%20%20%20%20%20park.simulate_hour()%0A%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20park%20%3D%20Park()%0A%20%20%20%20with%20open(%27data.json%27)%20as%20json_file%3A%0A%20%20%20%20%20%20%20%20data%20%3D%20json.load(json_file)%0A%20%20%20%20%20%20%20%20park.populate(data)%0A%20%20%20%20run(park))


## Running MonkeyType

[MonkeyType](https://pypi.org/project/MonkeyType/) is a automatic code inference tool. It collects runtime types of function arguments and return values, and can automatically generate stub files or even add draft type annotations directly to your Python code based on the types collected at runtime.

```
pip install MonkeyType
```

### Fix intentional exercise bugs

```
diff --git a/gradual_typing_project/main.py b/gradual_typing_project/main.py
index 1a622eb..01f27c8 100644
--- a/gradual_typing_project/main.py
+++ b/gradual_typing_project/main.py
@@ -7,16 +7,17 @@ def get_cat_dog_ratio(park):
     cats = len(park.inside_park["cats"])
     dogs = len(park.inside_park["dogs"])
     print(f"There are {cats} cats and {dogs} dogs in the park.")
-    return cats / dogs
+    if dogs > 0:
+        return cats / dogs


 def run(park):
     for hour in range(1, 9):
         print(f"Hour: {hour}")
         cat_dog_ratio = get_cat_dog_ratio(park)
-        dog_cat_ratio = 1 / cat_dog_ratio
-        print("Ratio of cats to dogs is " + cat_dog_ratio)
-        print("Ratio of dogs to cats is " + dog_cat_ratio)
+        dog_cat_ratio = None if not cat_dog_ratio else 1 / cat_dog_ratio
+        print("Ratio of cats to dogs is " + str(cat_dog_ratio))
+        print("Ratio of dogs to cats is " + str(dog_cat_ratio))
         park.simulate_hour()
```

### Run MonkeyType

```
(venv) szhu@szhu-mbp gradual_typing_project % monkeytype run main.py
Hour: 1
There are 4 cats and 3 dogs in the park.
Ratio of cats to dogs is 1.3333333333333333
Ratio of dogs to cats is 0.75
Hour: 2
There are 4 cats and 3 dogs in the park.
Ratio of cats to dogs is 1.3333333333333333
Ratio of dogs to cats is 0.75
Hour: 3
There are 2 cats and 4 dogs in the park.
Ratio of cats to dogs is 0.5
Ratio of dogs to cats is 2.0
Hour: 4
There are 2 cats and 5 dogs in the park.
Ratio of cats to dogs is 0.4
Ratio of dogs to cats is 2.5
Hour: 5
There are 3 cats and 4 dogs in the park.
Ratio of cats to dogs is 0.75
Ratio of dogs to cats is 1.3333333333333333
Hour: 6
There are 4 cats and 4 dogs in the park.
Ratio of cats to dogs is 1.0
Ratio of dogs to cats is 1.0
Courage and Piper get along!
Hour: 7
There are 2 cats and 4 dogs in the park.
Ratio of cats to dogs is 0.5
Ratio of dogs to cats is 2.0
Lucky and Piper get along!
Hour: 8
There are 2 cats and 4 dogs in the park.
Ratio of cats to dogs is 0.5
Ratio of dogs to cats is 2.0
Blue and Boo get along!
```

### Print Coverage Statistics (Before)

```
(venv) szhu@szhu-mbp gradual_typing_project % pyre statistics --print-summary
ƛ Coverage summary:
Overall annotation rate is 5.41%
There are 0 total error suppressions inline (0 fixmes and 0 ignores)
Of 4 modules, 0.0% are strict and 100.0% are unsafe
Of 17 functions, 0.0% are fully annotated and 0.0% are partially annotated
```

### Apply MonkeyType Stubs

```
(venv) szhu@szhu-mbp gradual_typing_project % monkeytype list-modules
pet
park
interact
(venv) szhu@szhu-mbp gradual_typing_project % monkeytype apply park
(venv) szhu@szhu-mbp gradual_typing_project % monkeytype apply interact
(venv) szhu@szhu-mbp gradual_typing_project % monkeytype apply pet
```

If you run into NameError problems, this means that an inferred annotation is referencing a class or value that has not been defiend yet. This pattern arises in `pet.py` and can be fixed by quoting any annotations that are forward-references.

### Print Coverage Statistics (After)

```
(venv) szhu@szhu-mbp gradual_typing_project % pyre statistics --print-summary
ƛ Coverage summary:
Overall annotation rate is 67.57%
There are 0 total error suppressions inline (0 fixmes and 0 ignores)
Of 4 modules, 0.0% are strict and 100.0% are unsafe
Of 17 functions, 64.71% are fully annotated and 0.0% are partially annotated
```
