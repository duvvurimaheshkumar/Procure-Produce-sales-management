---

# Producer App – Procurement Sales System

The **Producer** app is a Django module for managing producer (supplier) registrations and verifications within the Procurement Sales System. It provides forms for producer sign-up, admin tools for verification, and model logic for handling producer data and associated files.

---

## Features

- **Producer Registration:**  
  Producers can sign up by providing personal and contact information, uploading pictures and documents.
- **Admin Verification:**  
  Admins can view, filter, and verify/unverify producers from the Django admin interface. Upon verification, producers receive an email to set up their login credentials.
- **File Management:**  
  Uploaded pictures and documents are stored and properly deleted from the filesystem when a producer is removed.
- **Customizable Forms:**  
  The sign-up form is styled and can be extended as needed.

---

## Models

- **ProducerVerify:**  
  Temporary model for new sign-ups pending admin verification. Stores all producer details and uploads.
- **Producer:**  
  Main model for verified producers, linked to Django's `User` model for authentication.

Both models:
- Store personal, contact, and address information.
- Handle file uploads for pictures and documents.
- Include a `verified` status and creation timestamp.
- Delete associated files from disk when the record is deleted.

---

## Admin Interface

- **ProducerAdmin:**  
  - Displays key producer fields and verification status.
  - Allows filtering by verification status.
  - Provides actions to mark producers as verified/unverified.
  - Sends an email with a verification link when a producer is marked as verified.

---

## Forms

- **ProducerSignUpForm:**  
  Collects all necessary producer information and handles file uploads for registration.

---

## Views & URLs

- **producer:**  
  Renders the main producer page.
- **login:**  
  Renders the producer login page.
- **signUp:**  
  Handles GET (display form) and POST (process form) requests for producer registration. On successful registration, shows a success page.
- **success:**  
  Renders a simple success confirmation page.

**URL Patterns:**
- `/producer/` – Main producer page
- `/producer/login/` – Producer login
- `/producer/signup/` – Producer registration

---

## Email Verification

When an admin verifies a producer, an email is sent to the producer with a link to set up their username and password.  
- The email uses Django's `send_mail` function.
- The verification link points to the `loginCreation` view (ensure this URL is defined in your project).

---

## File Uploads

- **Pictures:** Saved to `media/producer_pictures/`
- **Documents:** Saved to `media/producer_documents/`
- Files are deleted from disk when the corresponding model instance is deleted.

---

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Admin Actions](https://docs.djangoproject.com/en/stable/ref/contrib/admin/actions/)
- [Django File Uploads](https://docs.djangoproject.com/en/stable/topics/http/file-uploads/)

---
