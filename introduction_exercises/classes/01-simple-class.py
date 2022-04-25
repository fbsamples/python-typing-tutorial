class Talk:
  """
  >>> str(Talk("Python Typing Tutorial", 13))
  '1 PM - Python Typing Tutorial'
  """

  # Step 1: Annotate the constructor.
  def __init__(self, title, hour):
      self.title = title
      self.hour = hour

  # Step 2: Annotate this method.
  def __str__(self):
      am_pm_string = "AM" if self.hour < 12 else "PM"
      return f"{self.hour % 12} {am_pm_string} - {self.title}"

# Step 3: Identity the bug present in one of these calls.
Talk("Python Typing Tutorial", "right now")
Talk("Python Typing Tutorial", 13)
