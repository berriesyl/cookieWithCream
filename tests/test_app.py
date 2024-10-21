import pytest
from app import app  # Flask uygulamanı import ediyoruz.

@pytest.fixture
def client():
    """Test için Flask uygulamasını başlat."""
    app.config['TESTING'] = True  # Testing modunu aktif edelim.
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Ana sayfanın doğru döndüğünü test et."""
    response = client.get("/")
    assert response.status_code == 200  # Sayfanın başarıyla döndüğünü kontrol eder.
    assert b"Cream-Filled Cookies Recipe" in response.data  # Başlık içeriyor mu?

def test_tasks_endpoint(client):
    """Tasks endpoint'inin JSON döndüğünü test et."""
    response = client.get("/tasks")
    assert response.status_code == 200  # Başarıyla çalışıyor mu?
    data = response.get_json()
    assert isinstance(data, list)  # JSON verisi bir liste mi?
    assert len(data) > 0  # Görev listesi boş değil mi?

def test_task_prerequisites():
    """Görevlerin ön koşullarını kontrol et."""
    tasks = [
        {"id": "mix-ingredients", "prerequisites": ["bring-ingredients"]},
        {"id": "bake-cookies", "prerequisites": ["preheat-oven", "shape-dough"]},
    ]
    for task in tasks:
        for prereq in task["prerequisites"]:
            assert any(t["id"] == prereq for t in tasks), f"Prerequisite {prereq} not met"

def test_total_time_calculation():
    """Toplam sürenin doğru hesaplandığını kontrol et."""
    tasks = [
        {"id": "prepare-cream", "time": 15, "prerequisites": []},
        {"id": "cool-cream", "time": 30, "prerequisites": ["prepare-cream"]},
    ]
    total_time = max(task["time"] for task in tasks)
    assert total_time == 30  # En uzun sürenin 30 dakika olduğundan emin olalım.
