from sitetaskexecutor.Gitproject._Gitproject.Gitproject import *

class Ln_Gitproject(
    Gitproject
):
    def NAME(self) -> str:
        return 'Ln'
    
    def pythonanywhere_username(self) -> str:
        return 'getln'

    def project_or_workshop(self) -> str:
        return 'project'

    def github_url_type(self) -> str:
        return 'ssh'

    def is_uninstall_as_package_supported(self) -> bool:
        return False

    def package_executables(self) -> List[str]:
        return []

    def additional_pythonpaths(self) -> List[str]:
        return []

    def clone_target_repository_for_site(self,
        PATHDIR_root_projektrepository:Path=None,
        URL_github_projekt_repository:str=None
    ) -> None:
        self._clone_target_repository_for_site_with_gitclone(
            PATHDIR_root_projektrepository=PATHDIR_root_projektrepository,
            URL_github_projekt_repository=URL_github_projekt_repository
        )