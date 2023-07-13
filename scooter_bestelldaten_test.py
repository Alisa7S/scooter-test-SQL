# Cоловьева Лариса, 6-я> когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

def test_get_order_track_number():
    track = sender_stand_request.post_new_order(data.order_body).json()["track"]
    response = sender_stand_request.get_track_order(track)
    assert response.status_code == 200
    print(response.json())
    print(response.status_code)



