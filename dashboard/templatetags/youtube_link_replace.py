from django import template


register = template.Library()


@register.simple_tag(name='youtube_link_replace')
def youtube_link_replace(lessoncontent):
    
    return lessoncontent.video_link.replace("https://www.youtube.com/watch?v=", "https://www.youtube.com/embed/")


