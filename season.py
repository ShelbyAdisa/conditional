def get_season(month):
    # Converts month name to number if it's a string
    if isinstance(month, str):
        month_names = ["january", "february", "march", "april", "may", "june", 
                       "july", "august", "september", "october", "november", "december"]
        month = month_names.index(month.lower()) + 1 if month.lower() in month_names else month
    
    # Make sure month is an integer between 1 and 12
    if not isinstance(month, int) or month < 1 or month > 12:
        return "Invalid month"
    
    # Determine season based on month number
    if month in [12, 1, 2]:
        
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:  # month in [9, 10, 11]
        return "Fall"

# Example usage
print(get_season(4))      
