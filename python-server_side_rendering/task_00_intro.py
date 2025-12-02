#!/usr/bin/python3
"""task"""


import os

def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders in {placeholder} format
        attendees (list): List of dictionaries containing attendee information
    
    Returns:
        None: Creates output files or logs error messages
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Check if all items in attendees are dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i} is not a dictionary.")
            return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Start with the template
        invitation = template
        
        # Define the placeholders we need to replace
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        # Replace each placeholder with the value from attendee or "N/A" if missing
        for placeholder in placeholders:
            # Get the value, use "N/A" if key doesn't exist or value is None
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            
            # Replace the placeholder in the template
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))
        
        # Create output filename
        output_filename = f"output_{i}.txt"
        
        # Write the invitation to file
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
            print(f"Created {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")


# For testing purposes (when run directly)
if __name__ == "__main__":
    # Example template (same as in template.txt)
    example_template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    # Example attendees data
    example_attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
        {"name": "Diana", "event_title": "Tech Meetup", "event_location": "Chicago"},  # Missing date
        {"name": "Eve"}  # Missing most fields
    ]
    
    # Test the function
    generate_invitations(example_template, example_attendees)
