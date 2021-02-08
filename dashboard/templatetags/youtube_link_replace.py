from django import template


register = template.Library()


@register.simple_tag(name='youtube_link_replace')
def youtube_link_replace(lessoncontent):
    video_link= lessoncontent.video_link.replace("https://www.youtube.com/watch?v=", "https://www.youtube.com/embed/")
    final_video_link = video_link.split('&list=')
    print(final_video_link[0])
    return final_video_link[0]

