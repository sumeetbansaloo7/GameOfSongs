from datetime import datetime
from pydantic import BaseModel
from fastapi import HTTPException


class Room(BaseModel):
    room_id: str
    # players :
    def __init__(self, id) -> None:
        self.room_id = id
        # players = []
        # chat_messages = []

    # def add_player(self, player_name):
    #     if player_name not in self.players:
    #         self.players.append(player_name)
    #     raise HTTPException(status_code=403, detail="Player Exists")

    # def send_message(self, player_name, message):
    #     if player_name not in self.players:
    #         raise HTTPException(status_code=403, detail="Player does not exists")
    #     new_message = {str(datetime.now): {player_name: message}}
    #     self.chat_messages.append(new_message)

    # def get_messages(self):
    #     return self.chat_messages
