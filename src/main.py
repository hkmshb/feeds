# from importlib import metadata


def get_version():
    """Returns the package version details."""
    # return metadata.version('feeds')
    return 2.1


def main():
    """Script entry point"""
    version = get_version()
    print(version)


main()