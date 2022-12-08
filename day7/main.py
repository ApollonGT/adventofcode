# import json
import pprint
pp = pprint.PrettyPrinter(depth=4)


class Structure:
    def __init__(self):
        self.files = {
            'path': '/',
            'size': 0,
            'content': [],
            'parent': None
        }

        self.current_location = self.files

    def __repr__(self):
        # pp.pprint(self.files)
        # print(json.dumps(self.files))

        print(f"{self.files['path']}: {self.files['size']}")
        self.print_children(self.files, 2)
        return f"Total: {self.files['size']}"

    def print_children(self, loc, ident=0):
        for f in loc['content']:
            print(' '*ident, end='')
            print(f"{f['path']}: {f['size']}")
            self.print_children(f, ident + 2)

    def add_size(self, sz):
        loc = self.current_location
        loc['size'] += sz
        while loc['parent'] is not None:
            loc = loc['parent']
            loc['size'] += sz

    def add_child(self, child):
        ch = child.split(' ')
        if ch[0] == 'dir':  # Directory
            new_dir = {
                'path': self.current_location['path'] + ch[1] + '/',
                'size': 0,
                'content': [],
                'parent': self.current_location
            }
            self.current_location['content'].append(new_dir)
        else:  # File
            sz = int(ch[0])
            new_file = {
                'path': self.current_location['path'] + ch[1],
                'size': sz,
                'content': [],
                'parent': self.current_location
            }
            self.current_location['content'].append(new_file)
            self.add_size(sz)

    def cd(self, ndir):
        if ndir == '/':
            self.current_location = self.files
            return

        if ndir == '..':
            self.current_location = self.current_location['parent']
            return

        fullpath = self.current_location['path'] + ndir + '/'
        idx = -1
        for i, d in enumerate(self.current_location['content']):
            if d['path'] == fullpath:
                idx = i
                break
        if idx >= 0:
            self.current_location = self.current_location['content'][idx]
        else:
            breakpoint()
            raise ValueError('Invalid Index')

    def find_dir_by_size(self, loc, min_sz=0, max_sz=100_000):
        res = []

        if loc is self.files and \
                self.files['size'] <= max_sz and self.files['size'] >= min_sz:
            res.append(("/", int(self.files['size'])))

        for f in loc['content']:
            if f['path'].endswith('/') and \
                    f['size'] <= max_sz and f['size'] >= min_sz:
                res.append((f"{f['path']}", int(f['size'])))
            res += self.find_dir_by_size(f, min_sz, max_sz)
        return res


def read_structure():
    files = Structure()
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            c_line = line.rstrip('\n')
            if c_line.startswith('$'):  # Command
                if 'cd' in c_line:
                    path = c_line.split(' ')
                    files.cd(path[2])
            else:  # List Item
                files.add_child(c_line)
    return files


if __name__ == "__main__":
    files = read_structure()

    # Part 1
    res = files.find_dir_by_size(files.files)
    res1 = sum([i[1] for i in res])
    print("Part 1: ", end="")
    print(res1)

    # Part 2
    total = 70_000_000
    required = 30_000_000
    used = int(files.files['size'])
    available = total - used
    must_free = required - available

    r = files.find_dir_by_size(files.files, min_sz=must_free, max_sz=required)
    r = sorted(r, key=lambda x: x[1])
    print("Part 2: ", end="")
    print(r[0])
