admin_permissions = {"read", "write", "delete", "manage_users"}
editor_permissions = {"read", "write"}

required_permissions = {"delete"}

can_perform = required_permissions.issubset(editor_permissions)

print(f"Can the editor perform the admin action? {can_perform}")