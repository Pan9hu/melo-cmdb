from api.account_api import AccountAPI
from api.audit_api import AuditAPI
from api.auth_api import AuthAPI
from api.config_repo_api import ConfigRepoAPI
from api.group_api import GroupAPI
from api.machine_api import MachineAPI
from api.res_pool_api import ResPoolAPI
from api.safe_group_api import SafeGroupAPI
from api.service_api import ServiceAPI
from api.task_api import TaskAPI
from api.overview_api import OverViewAPI
from core.server import Server
from core.settings import settings

Server.app.register_blueprint(AuthAPI.api)
Server.app.register_blueprint(GroupAPI.api)
Server.app.register_blueprint(AccountAPI.api)
Server.app.register_blueprint(AuditAPI.api)
Server.app.register_blueprint(ConfigRepoAPI.api)
Server.app.register_blueprint(MachineAPI.api)
Server.app.register_blueprint(ResPoolAPI.api)
Server.app.register_blueprint(SafeGroupAPI.api)
Server.app.register_blueprint(ServiceAPI.api)
Server.app.register_blueprint(TaskAPI.api)
Server.app.register_blueprint(OverViewAPI.api)

app = Server.app

if __name__ == '__main__':
    app.run(host=settings["listen"]["bind"], port=settings["listen"]["port"], debug=settings["debug"])
