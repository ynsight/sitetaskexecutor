from sitetaskexecutor.Gitproject._Gitproject.Gitproject import *

class letters_Gitproject(
    Gitproject
):
    def NAME(self) -> str:
        return 'letters'

    def pythonanywhere_username(self) -> str:
        return 'getletters'

    def project_or_workshop(self) -> str:
        return 'project'

    def github_url_type(self) -> str:
        return 'ssh'

    def is_uninstall_as_package_supported(self) -> bool:
        return True

    def package_executables(self) -> List[str]:
        return []
