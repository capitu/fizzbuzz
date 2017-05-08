from fabric.api import *
import xml.etree.ElementTree as ET
from fabric.colors import *

POM = 'pom.xml'
working_dir = "/Users/alsu/IdeaProjects/fizz/"


def getPomVersion():
    with lcd(working_dir):
        parser = PCParser()
        tree = ET.parse(working_dir + POM, parser=parser)
        root = tree.getroot()
        versionElement = root.find("{http://maven.apache.org/POM/4.0.0}version")
        return versionElement.text

def update_pom_version(dir, version):
    with lcd(dir):
        parser = PCParser()
        tree = ET.parse(dir + POM, parser=parser)
        root = tree.getroot()
        versionElement = root.find("{http://maven.apache.org/POM/4.0.0}version")
        #caso core
        if(versionElement is not None):
            update_version_element(versionElement, tree, dir, POM, version)
        parentElement = root.find("{http://maven.apache.org/POM/4.0.0}parent")
        #caso modulo
        if(parentElement is not None):
            print(yellow("changing parent version"))
            versionElement = parentElement.find("{http://maven.apache.org/POM/4.0.0}version")
            if(versionElement is not None):
                update_version_element(versionElement, tree, dir, POM, version)
            dependencies = root.find("{http://maven.apache.org/POM/4.0.0}dependencies")
            for dependency in dependencies:
                artefact = dependency.find("{http://maven.apache.org/POM/4.0.0}artifactId")
                if(artefact is not None):
                    if(artefact.text == "rio-core"):
                        versionElement = dependency.find("{http://maven.apache.org/POM/4.0.0}version")
                        if(versionElement is not None):
                            print(yellow("changing dependency version"))
                            update_version_element(versionElement, tree, dir, POM, version)



def update_version_element(versionElement, tree, dir, POM, version):
    current_version = versionElement.text
    next_version = str(version if version != '' else increment_version(current_version=current_version))
    versionElement.text = next_version
    print(green(versionElement.text))
    tree.write(dir + POM, encoding="UTF-8", default_namespace="http://maven.apache.org/POM/4.0.0")

def increment_version(current_version):
    # If it's a snapshot version, convert it to a release version
    #if current_version.endswith('-SNAPSHOT'):
    #return current_version[:-9]

    parts = current_version.split(".")
    last_part = parts[len(parts) - 1]
    try:
        # Add one to the final part of the version string
        incremented_last_part = str(int(last_part) + 1)
    except TypeError:
        raise InvalidVersion("Unsuppported version format [%s]" % current_version)

    # Try to maintain the zero padding of the old version, if any
    incremented_last_part = incremented_last_part.zfill(len(last_part))

    # Make it a snapshot version
    #incremented_last_part = incremented_last_part + '-SNAPSHOT'

    return ".".join(parts[:-1] + [incremented_last_part])

class InvalidVersion(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "Invalid version: " + self.msg

class PCParser(ET.XMLTreeBuilder):

    def __init__(self):
        ET.XMLTreeBuilder.__init__(self)
        # assumes ElementTree 1.2.X
        self._parser.CommentHandler = self.handle_comment

    def handle_comment(self, data):
        self._target.start(ET.Comment, {})
        self._target.data(data)
        self._target.end(ET.Comment)