# A plan for automating testing of a WebPages

**Task:**
Application testing (web-service), providing create a blogs with title and some content
1. Home Page
2. Blog Page
3. Post Page
4. New Post Page

### Precondition:
1. Launch an app on URL - http://127.0.0.1:5000

### Auto cases.

#### Content and Display:

**1. Correct display of the title on the Blog Page**
#### Steps:
1. Open Blog Page
2. Checking the Title on the Blog Page
3. Checking correctness the tag of the Title

**2. Correct display of the title on the Home Page**
#### Steps:
1. Open the Home Page
2. Checking the Title on the Home Page
3. Checking correctness the tag of the Title

**3. Correct display of the title on the New Post Page**
### Steps:
1. Open the New Post Page
2. Checking the Title on the New Post Page
3. Checking correctness the tag of the Title

**4. Successful display of created posts**
1. Open the Blog Page
2. Wait until posts to load

**5. Successful create a posts on Blog Page**
1. Open the Blog Page
2. Press the "Create Post" button
3. There is shown the Post Page
4. Enter "Test Post" in the "title" field
5. Enter "Test Content" in the content field
6. Press the "submit" button
7. There is shown Blog Page
8. Wait until posts to load
9. There is a post with title "Test Post" in the posts section

**6. Correct display of the title on the Post Page**
1. Open the Blog Page
2. Press the "Create Post" button
3. There is shown the Post Page
4. Enter "Test Post" in the "title" field
5. Enter "Test Content" in the content field
6. Press the "submit" button
7. There is shown Blog Page
8. Wait until posts to load
9. There is a post with title "Test Post2" in the posts section
10. Click on the new created post
11. Checking that the post was created
12. Checking that the title has a "Test Title2" title
13. Checking that the content has a "Test Content2" content

#### Navigation Between Pages

**1.Being on the Home Page, you can switch forward to Blog Page**
1. Open the Home Page
2. Click "Go to blog" button
3. There is shown BLog Page

**2. Being on the Blog Page, you can switch back to Home Page**
1. Open the Blog Page
2. Click "Go to home" button
3. There is shown Home Page

### Tools Used

- Asus VivoBook 14, core i5 - 10 gen.
- Python 3 - Popular programming language
- PyCharm 2023 1.4 - IDE
- Flask - Microframework
- Selenium - Is a web framework that permits you to execute cross-browser tests.

### Possible Risks in Automation

- Lack of documentation and clear technical specifications, which can lead to an error in the operation of a real application
- The total time spent on automation can exceed the total time of manual testing, and be very labor-intensive

### Interval risk assessment (in hours)

- Writing an automation plan: 1 hour;
- Test environment setup: 10 min;
- Writing and debugging autotests: 2 hours;

**Total: 2.5 hours**