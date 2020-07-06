from sitetaskexecutor.Gitproject._Gitproject.Gitproject import *


class fw_Gitproject(
    Gitproject
):
    def NAME(self) -> str:
        return 'fw'
    
    def pythonanywhere_username(self) -> str:
        return 'getfw'

    def project_or_workshop(self) -> str:
        return 'project'

    def github_url_type(self) -> str:
        return 'ssh'

    def is_uninstall_as_package_supported(self) -> bool:
        return True

    def package_executables(self) -> List[str]:
        return [
            'fw',
            'fw.sh',
            'fw.bat',
            'fw_.py',
            'fw.py'
        ]

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