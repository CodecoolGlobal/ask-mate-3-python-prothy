from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def sort_questions(cursor: RealDictCursor, order_by, order_direction):
    """Sorts questions by the given criteria, defaults to submission time"""
    query = f"""
        SELECT *
        FROM question
        ORDER BY {order_by} {order_direction}
    """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_answers_for_question(cursor: RealDictCursor, question_id):
    """Get all the answers for the selected question"""
    query = f"""
        SELECT *
        FROM answer
        WHERE question_id = {question_id}
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_question(cursor: RealDictCursor, question_id):
    """Lists all the questions """
    query = f"""
        SELECT *
        FROM question
        WHERE id = {question_id}
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def update_votes(cursor: RealDictCursor, vote_type: str, item_id, vote_action: str):
    """Updates vote count in database

    Parameters:
     vote_type - Table name to update ("question" or "answer")
     vote_action - "vote_up" or "vote_down"
    """
    calc_votes = "vote_number + 1" if vote_action == "vote_up" else "vote_number - 1"

    query = f"""
        UPDATE {vote_type}
        SET vote_number = {calc_votes} 
        WHERE id = {item_id}
    """

    cursor.execute(query)

@database_common.connection_handler
def update_view_count(cursor: RealDictCursor, question_id):
    """Updates the corresponding view count"""
    query = f"""
        UPDATE question
        SET view_number = view_number + 1
        WHERE id = {question_id}
    """
    cursor.execute(query)
