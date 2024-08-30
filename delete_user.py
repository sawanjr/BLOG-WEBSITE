# The `PendingRollbackError` you're encountering is due to a previous transaction failure that caused the session to roll back. The underlying issue is still related to the integrity constraint violation, specifically with the `post.user_id` field.

# Here's how you can handle this issue step-by-step in the Flask shell:

# ### Steps to Resolve the Issue

# 1. **Rollback the Current Session:**
#    - Since the session is in a rolled-back state, you need to issue a rollback to reset the session.

# 2. **Handle Related Records:**
#    - Before deleting users, you should address the foreign key constraint violation by updating or deleting related records.

# ### Commands to Run in Flask Shell

# 1. **Start Flask Shell:**
#    ```bash
#    flask shell
#    ```

# 2. **Import Necessary Modules and Rollback:**
#    ```python
#    from flaskblog import db
#    from flaskblog.models import User, Post

#    # Rollback the current session
#    db.session.rollback()
#    ```

# 3. **Define Emails to Keep and Query Users to Delete:**
#    ```python
#    emails_to_keep = ['sawanrawatjr10@gmail.com', 'amishachandra@gmail.com']
#    users_to_delete = User.query.filter(~User.email.in_(emails_to_keep)).all()
#    ```

# 4. **Delete or Update Related Records Before Deleting Users:**

#    - **Option 1: Delete Related Posts**
#      ```python
#      for user in users_to_delete:
#          # Delete related posts
#          Post.query.filter_by(user_id=user.id).delete()
         
#          # Delete the user
#          db.session.delete(user)

#      # Commit changes
#      db.session.commit()
#      ```

#    - **Option 2: Update Related Posts (Optional)**
#      ```python
#      for user in users_to_delete:
#          # Update related posts to set user_id to None
#          Post.query.filter_by(user_id=user.id).update({'user_id': None})

#          # Delete the user
#          db.session.delete(user)

#      # Commit changes
#      db.session.commit()
#      ```

# ### Summary of Steps

# 1. **Rollback** the current session to reset it.
# 2. **Handle** related `Post` records to avoid foreign key constraint issues.
# 3. **Delete** users and commit the changes.

# These steps should help you manage the foreign key constraints and resolve the integrity errors you’re encountering.