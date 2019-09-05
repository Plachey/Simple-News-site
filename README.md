# Simple-News-site

What is done!

1. Registration / authorization by e-mail
• Optional fields: First name, Last name, Age
• Checking the validity of mail and sending letters using services
https://www.mailgun.com/ or https://sendgrid.com/
• Validation of mail in a separate letter
2. Adding a post
• WYSIWYG editor to choose from (not relevant for API First)
• Ability to attach the application to the post
• Postponed post publication
3. Adding a comment to the post
• Ability to respond to comments (tree structure)
4. Admin panel
• Premoderation of posts
• Group of admins, editors and users (default)
• Ability to disable pre-moderation for a group of editors
• Ability to disable pre-moderation for certain
users regardless of group

5. Notifications of new comments
• When adding a comment
• Using the “subscribe” button. She’s the “unsubscribe” button,
if you are already subscribed

Requirements for the technical part:
• Python3
• Django
• Poetry for dependencies
