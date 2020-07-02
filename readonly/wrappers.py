def override_readonly(execute, sql, params, many, context):
    return execute(sql, params, many, context)
