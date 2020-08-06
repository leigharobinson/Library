# THis function is now called a view since it will handle HTTP requests
# urls.py will define which HTTP requests
from .home import home
from .books.list import book_list
from .books.form import book_form
from .librarians.list import librarian_list
from .libraries.list import library_list
from .libraries.form import library_form
from .auth.logout import logout_user
from .books.form import book_form
from .books.details import book_details
from .libraries.details import library_details
from .librarians.details import librarian_details
from .books.form import book_form, book_edit_form
