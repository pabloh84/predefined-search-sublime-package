import sublime
import sublime_plugin

SETTINGS_FILE = "PredefinedSearch.sublime-settings"

class PredefinedSearchCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings(SETTINGS_FILE)
        self.searches = settings.get("searches", [])

        if not self.searches:
            sublime.message_dialog("No predefined searches found.")
            return

        # Show the selection panel
        search_names = [search["name"] for search in self.searches]
        self.window.show_quick_panel(search_names, self.on_select)

    def on_select(self, index):
        if index == -1:
            return  # User cancelled

        search = self.searches[index]
        self.run_search(search)

    def run_search(self, search):
        # Show the Find in Files panel
        print("run_search", search)
        # self.window.run_command("show_panel", {"panel": "find_in_files"})
        self.window.run_command("show_panel", {
            "panel": "find_in_files",
            "pattern": search["pattern"],
            "where": search["where"],
            "whole_word": search["whole_word"],
            "regex": search["regex"],
            "case_sensitive": search["case_sensitive"],
            "replace_pattern": search["replace_pattern"],
            "preserve_case": True,
            "show_context": False,
            "use_buffer": False,
        })
