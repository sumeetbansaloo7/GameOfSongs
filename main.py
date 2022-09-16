from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import uuid

app = FastAPI()

game_rooms = {}


class Room:
    def __init__(self, id) -> None:
        self.room_id = id
        self.players = []
        self.chat_messages = []

    def add_player(self, player_name):
        if player_name not in self.players:
            self.players.append(player_name)
            return
        raise HTTPException(status_code=403, detail="Player Exists")


class ChatMessage(BaseModel):
    player: str
    message: str


@app.get("/create")
async def create_room():
    print("creating...")
    room_id = uuid.uuid4().hex[:8]
    new_game_room = Room(room_id)
    game_rooms[room_id] = new_game_room
    return new_game_room


@app.get("/join/{room_id}/{player_name}")
async def join_room(room_id, player_name):
    if room_id in game_rooms:
        current_room = game_rooms[room_id]
        current_room.add_player(player_name)
        return current_room
    raise HTTPException(status_code=403, detail="Room not found.")


@app.get("/room/{room_id}/")
async def get_players(room_id):
    if room_id in game_rooms:
        return game_rooms[room_id]
    raise HTTPException(status_code=403, detail="Room not found.")


@app.post("/message/{room_id}")
async def check_submission(chat_message: ChatMessage, room_id: str):
    print(room_id)
    print(chat_message.player)
    print(chat_message.message)
    return chat_message


# @app.get("/")
