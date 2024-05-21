def paginate_conversations(cursor):
    """
    Custom Function to paginate through conversations. Overrides the load_next_page method in the Cursor class.

    Args:
        cursor : Cursor object

    Returns:
        list : list of conversations
    """

    response = cursor._api._call(
        method="GET",
        path=cursor._path,
        data=cursor._params,
        token_data=cursor.token_data,
    )

    cursor._headers = response.headers

    body = response.json()
    cursor._queue = cursor._object_parser.parse_multiple(
        body, cursor._target_objects_class, cursor.token_data
    )
    if not cursor._queue:
        return False

    sort_by = cursor._params.get("sortBy")
    if not sort_by:
        return False

    cursor._params["startAfterDate"] = cursor._queue[-1].get("lastMessageDate")
    return True


def paginate_messages(cursor):
    """
    Custom Function to paginate through messages. Overrides the load_next_page method in the Cursor class.

    Args:
        cursor : Cursor object

    Returns:
        list : list of messages
    """

    response = cursor._api._call(
        method="GET",
        path=cursor._path,
        data=cursor._params,
        token_data=cursor.token_data,
    )

    cursor._headers = response.headers

    body = response.json()
    messages = body.get("messages")
    if not messages:
        return False

    cursor._queue = cursor._object_parser.parse_multiple(
        messages, cursor._target_objects_class, cursor.token_data
    )

    next_page = messages.get("nextPage")
    cursor._has_next_page = next_page

    last_message_id = messages.get("lastMessageId")
    cursor._params["lastMessageId"] = last_message_id

    if not cursor._has_next_page:
        return False
    return True
