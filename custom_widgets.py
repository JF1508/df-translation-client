import tkinter as tk
import tkinter.ttk as ttk


class CheckbuttonVar(ttk.Checkbutton):
    def __init__(self, *args, **kwargs):
        self._var = tk.BooleanVar()
        super().__init__(*args, variable=self._var, **kwargs)

    @property
    def is_checked(self):
        return self._var.get()

    @is_checked.setter
    def is_checked(self, value):
        self._var.set(value)


class EntryCustom(ttk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _set(self, value):
        self.delete(0, tk.END)
        self.insert(0, value)

    @property
    def text(self):
        return self.get()

    @text.setter
    def text(self, value: str):
        self._set(value)


class ComboboxCustom(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set(self, value):
        self.delete(0, tk.END)
        self.insert(0, value)

    @property
    def text(self):
        return self.get()

    @text.setter
    def text(self, value: str):
        self._set(value)

    @property
    def values(self):
        return self['values']

    @values.setter
    def values(self, values: tuple):
        self['values'] = values


class ListboxCustom(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        yscrollbar = ttk.Scrollbar(self)
        xscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)

        self._var = tk.Variable()
        self._listbox = tk.Listbox(self, *args,
                                   listvariable=self._var,
                                   xscrollcommand=xscrollbar.set,
                                   yscrollcommand=yscrollbar.set,
                                   **kwargs)

        yscrollbar['command'] = self._listbox.yview
        xscrollbar['command'] = self._listbox.xview

        xscrollbar.pack(side='bottom', fill='x')
        yscrollbar.pack(side='right', fill='y')
        self._listbox.pack(fill='both', expand=1)

    @property
    def values(self):
        return self._var.get()

    @values.setter
    def values(self, values: tuple):
        self._var.set(values)

    def clear(self):
        self._listbox.delete(0, tk.END)

    def curselection(self):
        return self._listbox.curselection()
