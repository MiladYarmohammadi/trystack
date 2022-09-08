from flask_restful import Resource

from trystack.controller.apiv1 import ProjectController


class ProjectResource(Resource):
    """
    GET /projects --> Project List
    GET /projects/<project_id> --> Project Info
    """

    def get(self, project_id=None):
        if project_id is None:
            return ProjectController.get_projects()
        else:
            return ProjectController.get_project(project_id)

    """
    POST /projects --> Create a New Project
    POST /projects/<project_id> --> Not Allowed
    """

    def post(self):
        return ProjectController.create_project()

    """
    PATCH /projects --> Not Allowed
    PATCH /projects/<project_id> --> Update Project
    """

    def patch(self, project_id):
        return ProjectController.update_project(project_id)

    """
    DELETE /projects --> Not Allowed
    DELETE /projects/<project_id> --> Delete Project
    """

    def delete(self, project_id):
        return ProjectController.delete_project(project_id)
