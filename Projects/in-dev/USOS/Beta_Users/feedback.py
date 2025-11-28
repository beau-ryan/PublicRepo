from datetime import datetime


class FeedbackRequest:
    def __init__(self, user_id, feedback_text, priority="normal", tags=None, metadata=None):
        self.user_id = user_id
        self.feedback_text = feedback_text
        self.status = "pending"
        self.timestamp = datetime.now()
        self.priority = priority
        self.tags = tags if tags is not None else []
        self.metadata = metadata if metadata is not None else {}
        self.response = None
        self.rating = None

    def __repr__(self):
        return (f"<FeedbackRequest user_id={self.user_id} "
                f"feedback_text={self.feedback_text[:200]}... status={self.status} "
                f"timestamp={self.timestamp.isoformat()}>")

    def __str__(self):
        return (f"Feedback from {self.user_id}: {self.feedback_text} "
                f"(Status: {self.status}, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})")
    
    def add_response(self, response_text, rating=None):
        self.response = response_text
        self.rating = rating
        self.status = "addressed"

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def log_metadata(self, key, value):
        self.metadata[key] = value

    def mark_as_reviewed(self):
        self.status = "reviewed"

    def mark_as_pending(self):
        self.status = "pending"

    def mark_as_addressed(self):
        self.status = "addressed"

    def is_high_priority(self):
        return self.priority == "high"
    
    def summary(self):
        return {
            "user_id": self.user_id,
            "feedback_text": self.feedback_text,
            "status": self.status,
            "timestamp": self.timestamp.isoformat(),
            "priority": self.priority,
            "tags": self.tags,
            "metadata": self.metadata,
            "response": self.response,
            "rating": self.rating
        }
    def clear_response(self):
        self.response = None
        self.rating = None
        self.status = "pending"

    def update_feedback_text(self, new_text):
        self.feedback_text = new_text
        self.timestamp = datetime.now()

    def has_tag(self, tag):
        return tag in self.tags
    
    def remove_tag(self, tag):

        if tag in self.tags:
            self.tags.remove(tag)

    def set_priority(self, priority):

        self.priority = priority

    def get_metadata(self, key):

        return self.metadata.get(key)
    
    def clear_metadata(self):

        self.metadata = {}
    def get_age_in_days(self):

        delta = datetime.now() - self.timestamp
        return delta.days
    
    def is_addressed(self):

        return self.status == "addressed"
    
    def is_reviewed(self):

        return self.status == "reviewed"
    
    def is_pending(self):

        return self.status == "pending"
    
    def mark_as_high_priority(self):

        self.priority = "high"

    def mark_as_normal_priority(self):

        self.priority = "normal"

    def get_response(self):
        return self.response
    
    def get_rating(self):

        return self.rating
    
    def has_response(self):

        return self.response is not None
    
    def has_rating(self):

        return self.rating is not None
    
    def to_dict(self):
        return self.summary()
    
    def from_dict(self, data):  
        self.user_id = data.get("user_id", self.user_id)
        self.feedback_text = data.get("feedback_text", self.feedback_text)
        self.status = data.get("status", self.status)
        self.timestamp = datetime.fromisoformat(data.get("timestamp")) if data.get("timestamp") else self.timestamp
        self.priority = data.get("priority", self.priority)
        self.tags = data.get("tags", self.tags)
        self.metadata = data.get("metadata", self.metadata)
        self.response = data.get("response", self.response)
        self.rating = data.get("rating", self.rating)

    def duplicate(self):
        new_instance = FeedbackRequest(
            user_id=self.user_id,
            feedback_text=self.feedback_text,
            priority=self.priority,
            tags=self.tags.copy(),
            metadata=self.metadata.copy()
        )
        new_instance.status = self.status
        new_instance.timestamp = self.timestamp
        new_instance.response = self.response
        new_instance.rating = self.rating
        return new_instance
    
    def clear_tags(self):
        self.tags = []

    def clear_priority(self):
        self.priority = "normal"

    def clear_status(self):
        self.status = "pending"

    def reset(self):
        self.clear_response()
        self.clear_tags()
        self.clear_metadata()
        self.clear_priority()
        self.clear_status()

    def extend_tags(self, new_tags):

        for tag in new_tags:
            if tag not in self.tags:
                self.tags.append(tag)

    def update_metadata(self, new_metadata):

        self.metadata.update(new_metadata)

    def get_tag_count(self):

        return len(self.tags)
    
    def get_metadata_keys(self):
        return list(self.metadata.keys())
    
    def get_metadata_values(self):
        return list(self.metadata.values())
    
    def print_summary(self):
        print(f"Feedback Summary:\n"
              f"User ID: {self.user_id}\n"
              f"Feedback Text: {self.feedback_text}\n"
              f"Status: {self.status}\n"
              f"Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
              f"Priority: {self.priority}\n"
              f"Tags: {', '.join(self.tags)}\n"
              f"Metadata: {self.metadata}\n"
              f"Response: {self.response}\n"
              f"Rating: {self.rating}")
        
    def print_brief(self):
        print(f"Feedback from {self.user_id}: {self.feedback_text[:30]}... (Status: {self.status})")

    def mark_as_urgent(self):
        self.priority = "high"