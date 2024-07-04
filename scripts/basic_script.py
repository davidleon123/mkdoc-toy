import mkdocs_gen_files

filename = "foo.md"

with mkdocs_gen_files.open(filename, "w") as f:
    print("Hello, world!", file=f)

#mkdocs_gen_files.set_edit_path(filename, "scripts/basic_script.py")

