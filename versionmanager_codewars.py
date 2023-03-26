class VersionManager:
    # null.object
    def __init__(self, version=''):
        self.versioncontrol = []
        # --------------
        self.MAJOR = 0
        self.MINOR = 0
        self.PATCH = 0
        # --------------

        if not version:
            self.PATCH += 1
            self.versioncontrol.append([self.MAJOR, self.MINOR, self.PATCH])
            return
        else:
            if [i for i in version.split('.')[:3] if not (i.isdigit())]:
                raise TypeError('Error occured while parsing version!')
            self.version = list(map(int, version.split('.')[:3]))
            while len(self.version) != 3:
                self.version.append(0)

            # --------------------------
            self.MAJOR = self.version[0]
            self.MINOR = self.version[1]
            self.PATCH = self.version[2]
            # --------------------------
            self.versioncontrol.append([self.MAJOR, self.MINOR, self.PATCH])

    def release(self):
        return '.'.join([str(self.MAJOR), str(self.MINOR), str(self.PATCH)])

    def major(self):
        self.PATCH = 0
        self.MINOR = 0
        self.MAJOR += 1
        self.versioncontrol.append([self.MAJOR, self.MINOR, self.PATCH])
        return self

    def minor(self):
        self.PATCH = 0
        self.MINOR += 1
        self.versioncontrol.append([self.MAJOR, self.MINOR, self.PATCH])
        return self

    def patch(self):
        self.PATCH += 1
        self.versioncontrol.append([self.MAJOR, self.MINOR, self.PATCH])
        return self

    def rollback(self):
        if len(self.versioncontrol) > 1:
            self.versioncontrol = self.versioncontrol[:-1]
            self.MAJOR = self.versioncontrol[-1][0]
            self.MINOR = self.versioncontrol[-1][1]
            self.PATCH = self.versioncontrol[-1][2]
            return self
        else:
            raise Exception("Cannot rollback!")
