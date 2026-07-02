"""
Internationalization module for bilingual support (English/Persian)
English is the default language.
"""

from enum import Enum
from typing import Dict, Any


class Language(Enum):
    ENGLISH = "en"
    PERSIAN = "fa"


# Translation dictionary
TRANSLATIONS: Dict[Language, Dict[str, str]] = {
    Language.ENGLISH: {
        # Main window
        "app_title": "My Application",
        "welcome_title": "Welcome to My Application",

        # Menu
        "menu_file": "File",
        "menu_info": "Information",
        "menu_add_info": "Add Information",
        "menu_exit": "Exit",
        "menu_language": "Language",
        "menu_english": "English",
        "menu_persian": "Persian",

        # Top level window
        "toplevel_title": "Register Information",
        "frame_records": "Registered Records",
        "frame_form": "Information Form",

        # Treeview columns
        "col_id": "ID",
        "col_name": "Name",
        "col_family": "Family Name",
        "col_age": "Age",
        "col_date": "Date",

        # Form labels
        "label_name": "Name",
        "label_family": "Family Name",
        "label_age": "Age",

        # Buttons
        "btn_save_new": "Save New",
        "btn_update": "Update",
        "btn_delete": "Delete",
        "btn_clear": "Clear",

        # Messages
        "error_invalid_data": "Please enter valid information",
        "error_invalid_age": "Age must be a number",
        "error_invalid_age_range": "Age must be between 1 and 150",
        "warning_no_selection": "No record selected",
        "info_no_changes": "No changes made",
        "error_save_failed": "Failed to save record",
        "error_delete_failed": "Failed to delete record",
        "error_update_failed": "Failed to update record",
        "error_file_operation": "File operation failed",
        "confirm_delete": "Are you sure you want to delete this record?",
        "confirm_update": "Are you sure you want to update this record?",

        # Form placeholders
        "placeholder_name": "Enter name",
        "placeholder_family": "Enter family name",
        "placeholder_age": "Enter age",

        # Date format
        "date_format": "%Y/%m/%d %H:%M",

        # Excel headers
        "excel_id": "ID",
        "excel_name": "Name",
        "excel_family": "Family Name",
        "excel_age": "Age",
        "excel_date": "Date",
    },
    Language.PERSIAN: {
        # Main window
        "app_title": "برنامه من",
        "welcome_title": "به برنامه من خوش آمدید",

        # Menu
        "menu_file": "فایل",
        "menu_info": "اطلاعات",
        "menu_add_info": "اضافه کردن اطلاعات",
        "menu_exit": "خروج",
        "menu_language": "زبان",
        "menu_english": "انگلیسی",
        "menu_persian": "فارسی",

        # Top level window
        "toplevel_title": "ثبت اطلاعات",
        "frame_records": "رکوردهای ثبت شده",
        "frame_form": "فرم اطلاعات",

        # Treeview columns
        "col_id": "ردیف",
        "col_name": "نام",
        "col_family": "نام خانوادگی",
        "col_age": "سن",
        "col_date": "تاریخ",

        # Form labels
        "label_name": "نام",
        "label_family": "نام خانوادگی",
        "label_age": "سن",

        # Buttons
        "btn_save_new": "ذخیره جدید",
        "btn_update": "ویرایش",
        "btn_delete": "حذف",
        "btn_clear": "پاک کردن",

        # Messages
        "error_invalid_data": "اطلاعات معتبر وارد کنید",
        "error_invalid_age": "سن باید عدد باشد",
        "error_invalid_age_range": "سن باید بین ۱ تا ۱۵۰ باشد",
        "warning_no_selection": "رکوردی انتخاب نشده",
        "info_no_changes": "هیچ تغییری اعمال نشده",
        "error_save_failed": "ذخیره رکورد با خطا مواجه شد",
        "error_delete_failed": "حذف رکورد با خطا مواجه شد",
        "error_update_failed": "بروزرسانی رکورد با خطا مواجه شد",
        "error_file_operation": "عملیات فایل با خطا مواجه شد",
        "confirm_delete": "آیا از حذف این رکورد مطمئن هستید؟",
        "confirm_update": "آیا از ویرایش این رکورد مطمئن هستید؟",

        # Form placeholders
        "placeholder_name": "نام را وارد کنید",
        "placeholder_family": "نام خانوادگی را وارد کنید",
        "placeholder_age": "سن را وارد کنید",

        # Date format (Jalali)
        "date_format": "%Y/%m/%d %H:%M",

        # Excel headers
        "excel_id": "ردیف",
        "excel_name": "نام",
        "excel_family": "نام خانوادگی",
        "excel_age": "سن",
        "excel_date": "تاریخ",
    },
}


# Current language state
_current_language = Language.ENGLISH


def set_language(lang: Language) -> None:
    """Set the current language."""
    global _current_language
    _current_language = lang


def get_language() -> Language:
    """Get the current language."""
    return _current_language


def t(key: str) -> str:
    """Translate a key to the current language."""
    return TRANSLATIONS[_current_language].get(key, key)


def get_excel_headers() -> list:
    """Get Excel headers for current language."""
    lang = get_language()
    return [
        TRANSLATIONS[lang]["excel_id"],
        TRANSLATIONS[lang]["excel_name"],
        TRANSLATIONS[lang]["excel_family"],
        TRANSLATIONS[lang]["excel_age"],
        TRANSLATIONS[lang]["excel_date"],
    ]


def get_date_format() -> str:
    """Get date format for current language."""
    return TRANSLATIONS[_current_language]["date_format"]


def get_language_name(lang: Language) -> str:
    """Get display name for a language in current language."""
    if lang == Language.ENGLISH:
        return "English" if _current_language == Language.ENGLISH else "انگلیسی"
    return "Persian" if _current_language == Language.ENGLISH else "فارسی"