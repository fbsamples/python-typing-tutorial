class Talk:
  """
  >>> str(Talk("Python Typing Tutorial", 13))
  '1 PM - Python Typing Tutorial'
  """

  # Step 1: Annotate the constructor.
  # Look at the above docstring to figure out what types they should be.
  def __init__(self, title: str, hour: int) -> None:
      self.title = title
      self.hour = hour

  # Step 2: Annotate this method.
  def __str__(self) -> str:
      am_pm_string = "AM" if self.hour < 12 else "PM"
      return f"{self.hour % 12} {am_pm_string} - {self.title}"

# Step 3: Identify the bug in following code.
print("When does the tutorial begin?")
hour = input()
tutorial = Talk("Python Typing Tutorial", hour)
other_tutorial = Talk("Tutorial you'll have to catch later on YouTube", 13)
print(tutorial)
print(other_tutorial)

# Step 4: If you have time, run this code in a terminal to see what error you
# get. Was it easy to figure out your error from that error message?
