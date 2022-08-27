from trystack.util.jsonify import jsonify


class ProjectController:
    def get_projects():
        return jsonify(status=501)

    def get_project(project_id=None):
        return jsonify(status=501)

    def create_project():
        return jsonify(status=501)

    def patch_project(project_id=None):
        return jsonify(status=501)

    def delete_project(project_id=None):
        return jsonify(status=501)
