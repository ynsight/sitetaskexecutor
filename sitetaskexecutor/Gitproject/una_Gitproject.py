from sitetaskexecutor.Gitproject._Gitproject.Gitproject import *

class una_Gitproject(
    Gitproject
):
    def NAME(self) -> str:
        return 'una'

    def pythonanywhere_username(self) -> str:
        return 'getuna'

    def project_or_workshop(self) -> str:
        return 'project'

    def github_url_type(self) -> str:
        return 'ssh'

    def is_uninstall_as_package_supported(self) -> bool:
        return True

    def package_executables(self) -> List[str]:
        return [
            'una',
            'una.sh',
            'una.bat',
            'una_.py',
            'una.py'
        ]

    def additional_pythonpaths(self) -> List[str]:
        return [
            str(self.task().PATHDIR_root() / Path(self.NAME(), 'src', 'una', 'lib')),
            str(self.task().PATHDIR_root() / Path(self.NAME(), 'src', 'una_factory', 'lib')),
        ]

    def clone_target_repository_for_site(self,
        PATHDIR_root_projektrepository:Path=None,
        URL_github_projekt_repository:str=None
    ) -> None:
        self._clone_target_repository_for_site_with_gitclone(
            PATHDIR_root_projektrepository=PATHDIR_root_projektrepository,
            URL_github_projekt_repository=URL_github_projekt_repository
        )

    def sitepub_github_dirs(self) -> List[str]:
        return [
            '_projekt'
        ]

    def sitepub_github_files(self) -> List[str]:
        return [
            'LICENSE.txt',
            'README.md',
            'VERSION',
            'make_sitepub.py'
        ]